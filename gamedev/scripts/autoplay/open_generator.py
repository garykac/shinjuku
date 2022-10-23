from game_data import GameData
from game_state import GameState
from generator import CandidateGenerator
from logger import Logger

class OpenStoreCandidateGenerator(CandidateGenerator):
	def __init__(self, data: GameData, gs: GameState, logger: Logger) -> None:
		self.data = data
		self.game_state = gs
		self.logger = logger

	def find_candidates(self, player_id: int) -> list[dict]:
		candidates = []
		candidates.extend(self.find_station(player_id))
		return candidates

	def find_station(self, player_id: int) -> list[dict]:
		gs = self.game_state
		player = gs.get_player(player_id)
		hand = player.get_hand()
		checked_wards = []
		candidates = []
		for ward in hand:
			if ward in checked_wards:
				continue
			checked_wards.append(ward)

			# Skip if we already have a store in this ward.
			player_has_store_here_already: bool = False
			for station in self.data.ward_stations[ward]:
				if not gs.is_empty_station(station):
					(store_type, owner_id) = gs.get_station_info(station)
					if owner_id == player_id:
						player_has_store_here_already = True
			if player_has_store_here_already:
				continue

			ward_score = 0
			# More ward cards in deck means more wildcard opportunities.
			ward_score += self.data.ward_cards[ward]
			# Multiple copies of a card -> wildcard once you open a store there.
			if hand.count(ward) > 1:
				ward_score += 4

			for station in self.data.ward_stations[ward]:
				# Check if station is unoccupied.
				if not gs.is_empty_station(station):
					continue

				station_score = ward_score
				# Stations that can be upgraded to dept stores.
				if station in self.data.dept_store_stations:
					station_score += 6
				# Stations with lots of connections.
				station_score += len(self.data.station_connections[station])
				# TODO: Stations that are the only one in that ward.

				# Evaluate each store type.
				for store_type, count in player.stores.items():
					# Make sure player still has a store of that type available.
					if count == 0:
						continue

					score = station_score
					# Store matches customers already in ward.
					score += gs.bonus_for_ward_customers(ward, store_type)
					# TODO: what customer type is the player looking for to complete a set.

					candidates.append({
						'action': "OPEN",
						'type': store_type,
						'station': station,
						'ward': ward,
						'score': score,
						})

		return candidates
