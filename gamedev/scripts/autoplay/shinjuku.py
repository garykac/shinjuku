#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import os
import random
import sys

from game_data import GameData
from game_state import GameState
from logger import Logger
from player import Player
from typing import Optional

from expand_generator import ExpandTrackCandidateGenerator
from generator import CandidateGenerator
from income_generator import IncomeCandidateGenerator
from move_generator import MoveCustomerCandidateGenerator
from open_generator import OpenStoreCandidateGenerator
from upgrade_generator import UpgradeStoreCandidateGenerator

class Shinjuku:
	def __init__(self, log_options: dict[str, bool]) -> None:
		self.log_options = log_options
		
		self.logger= Logger()
		self.data = GameData()
		self.game_state = GameState(self.data, self.logger, log_options)

		self.open_generator = OpenStoreCandidateGenerator(self.data, self.game_state, self.logger)		
		self.expand_generator = ExpandTrackCandidateGenerator(self.data, self.game_state, self.logger)		
		self.income_generator = IncomeCandidateGenerator(self.data, self.game_state, self.logger)		
		self.move_generator = MoveCustomerCandidateGenerator(self.data, self.game_state, self.logger)		
		self.upgrade_generator = UpgradeStoreCandidateGenerator(self.data, self.game_state, self.logger)		

		self.action_generators: dict[str, CandidateGenerator] = {
			"OPEN": self.open_generator,
			"EXPAND": self.expand_generator,
			"INCOME": self.income_generator,
			"MOVE": self.move_generator,
			"UPGRADE": self.upgrade_generator,
		}

		self.num_players: int = 0
		self.player_turn = 0

	def log(self, msg: str) -> None:
		self.logger.log(msg)	

	def indent(self, n: int) -> None:
		self.logger.indent(n)

	def log_candidates(self, actions: list[dict]) -> None:
		for action in actions:
			self.log_candidate(action)

	def log_candidate(self, action: dict) -> None:
		if action['action'] == "OPEN":
			self.log(f"OPEN {action['type']} {action['station']} {action['ward']} {action['score']}")
		if action['action'] == "EXPAND":
			self.log(f"EXPAND {action['station']} - {action['target']} {action['score']}")
		if action['action'] == "INCOME":
			self.log(f"INCOME {action['score']}")
		if action['action'] == "MOVE":
			self.log(f"MOVE {action['ward']} {action['stations']} {action['score']}")
	
	def setup_game(self, num_players: int) -> None:
		self.num_players = num_players
		self.game_state.init_ward_deck()
		self.game_state.init_customer_bag()
		self.game_state.init_customer_queue()
		self.game_state.init_gameboard()
		self.game_state.add_seed_customers()
		
		for i in range(num_players):
			player_id = self.game_state.add_player()
			self.game_state.draw_hand(player_id)

	def play(self) -> None:
		first_player = self.game_state.get_first_player()
		self.player_turn = 0
		player_id = first_player
		# TODO: game play until last customer is placed on map
		while len(self.game_state.customer_bag) != 0:
		#for i in range(9):
			self.player_turn += 1
			self.handle_turn(player_id)
			player_id += 1
			if player_id > self.num_players:
				player_id = 1
		
		# Ensure each player has the same number of turns.
		while player_id != first_player:
			self.player_turn += 1
			self.handle_turn(player_id)
			player_id += 1
			if player_id > self.num_players:
				player_id = 1
		
		self.log("Game over")
	
	def handle_turn(self, player_id: int) -> None:
		self.log("")
		self.log(f"*** Turn {self.player_turn}: Player {player_id}")
		self.indent(1)
		num_customers = self.game_state.place_customers_from_queue(player_id)
		self.game_state.refresh_queue(num_customers)
		
		if self.log_options['player-info']:
			self.game_state.log_player_hand(player_id)
			self.game_state.log_player_components(player_id)
			self.game_state.log_player_customers(player_id)
		if self.log_options['map-info']:
			self.game_state.log_map_customers()
			self.game_state.log_map_stations()
			self.game_state.log_map_connections()

		available_actions = ["OPEN", "EXPAND", "INCOME", "MOVE", "UPGRADE"]
		self.log(f"Action 1:")
		self.indent(1)
		action = self.evaluate_actions(available_actions, player_id)
		self.perform_action(action, player_id)
		self.indent(-1)

		self.log(f"Action 2:")
		self.indent(1)
		first_action = action['action']
		if first_action == "INCOME":
			self.log("SKIP")
		else:
			available_actions.remove(first_action)
			action = self.evaluate_actions(available_actions, player_id)
			self.perform_action(action, player_id)
		self.indent(-1)
		
		self.indent(-1)
		self.game_state.log_queue()
		
	def evaluate_actions(self, available_actions: list[str], player_id: int) -> dict:
		all_candidates = []
		for action in available_actions:
			all_candidates += self.action_generators[action].find_candidates(player_id)

		# TODO: Choose randomly if multiple candidates are tied at the top.
		sorted_candidates = sorted(all_candidates, key=lambda x: x['score'], reverse=True)
		if self.log_options['candidates']:
			self.log_candidates(sorted_candidates)
		return sorted_candidates[0]

	def perform_action(self, action: dict, player_id: int) -> None:
		gs = self.game_state
		a = action['action']
		if a == "OPEN":
			store_type = action['type']
			station = action['station']
			gs.open_store_in_station(station, store_type, player_id)
			return
		if a == "EXPAND":
			station = action['station']
			target = action['target']
			gs.add_connection(station, target, player_id)
			return
		if a == "INCOME":
			gs.draw_income(player_id)
			return
		if a == "MOVE":
			ward = action['ward']
			stations = action['stations']
			gs.move_customers(ward, stations, player_id)
			return
	
def usage():
	print("Usage: %s <options>" % sys.argv[0])
	print("where <options> are:")
	print("  --players <num>  [-p]")
	print("  --log-player-info")
	print("  --log-map-info")
	print("  --log-candidates")
	exit()

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:],
			'p:h',
			['players=', 'help', 'verbose', 'log-player-info', 'log-map-info', 'log-candidates'])
	except getopt.GetoptError:
		usage()

	players = 3
	verbose = False
	log_options: dict[str, bool] = {
		'player-info': False,
		'map-info': False,
		'candidates': False,
		'initial-setup': False,
	}
	
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
		if opt in ('-p', '--players'):
			players = int(arg)
		if opt == '--log-player-info':
			log_options['player-info'] = True
		if opt == '--log-map-info':
			log_options['map-info'] = True
		if opt == '--log-candidates':
			log_options['candidates'] = True
		if opt == '--log-initial-setup':
			log_options['initial-setup'] = True

	#seed = random.randint(0, 65536)
	seed = 31545
	#print(seed)
	random.seed(seed)

	s = Shinjuku(log_options)
	s.setup_game(players)
	s.play()

if __name__ == '__main__':
	main()
