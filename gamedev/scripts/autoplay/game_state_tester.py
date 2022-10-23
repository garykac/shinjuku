from game_data import GameData
from game_state import GameState
from logger import Logger

from expand_generator import ExpandTrackCandidateGenerator
from open_generator import OpenStoreCandidateGenerator
from move_generator import MoveCustomerCandidateGenerator

class GameStateTester():
	def __init__(self):
		self.log_options: dict[str, bool] = {
			'player-info': False,
			'map-info': False,
			'candidates': False,
			'initial-setup': False,
		}
		self.logger = Logger()
		self.data = GameData()
		self.gs = GameState(self.data, self.logger, self.log_options)
		self.player_id = self.gs.add_player()
		self.opponent_id = self.gs.add_player()
		
		self.open_gen = OpenStoreCandidateGenerator(self.data, self.gs, self.logger)	
		self.expand_gen = ExpandTrackCandidateGenerator(self.data, self.gs, self.logger)	
		self.move_gen = MoveCustomerCandidateGenerator(self.data, self.gs, self.logger)	
	
	@staticmethod
	def newBuilder() -> "GameStateTester":
		return GameStateTester()

	def assert_ward(self, ward):
		assert ward in self.data.ward_cards, "Invalid ward"
	
	def assert_station(self, station):
		assert station in self.data.station_wards, "Invalid station"

	def assert_store(self, store):
		assert store in self.data.CUSTOMER_TYPES, "Invalid store"

	def assert_customer(self, customer):
		assert customer in self.data.customer_type_rank, "Invalid customer"

	# Verify that 2 sets of customers match exactly.
	def verify_customers_match(self, cust1: list[str], cust2: list[str]):
		d1 = {}
		for c in cust1:
			if not c in d1:
				d1[c] = 0
			d1[c] += 1
	
		d2 = {}
		for c in cust2:
			if not c in d2:
				d2[c] = 0
			d2[c] += 1

		for c in d1.keys():
			assert d1[c] == d2[c]
		for c in d2.keys():
			assert d2[c] == d1[c]

	# Verify that |preferred-station| has a higher score then |other_station| in the
	# candidate list.
	def verify_open_preferred_store_location(self, candidates, preferred_station, other_station):
		score1 = 0
		score2 = 0
		for c in candidates:
			if not c['action'] == "OPEN":
				continue
			if c['station'] == preferred_station:
				score1 = c['score']
			if c['station'] == other_station:
				score2 = c['score']
		assert score1 > score2

	# Verify that |preferred_store| has a higher score then any other store in the
	# candidate list for this |station|.
	def verify_open_preferred_store_type(self, candidates, station, preferred_store):
		score_pref = 0
		score_other = 0
		for c in candidates:
			if not c['action'] == "OPEN":
				continue
			if c['station'] == station:
				score = c['score']
				if c['type'] == preferred_store:
					score_pref = score
				else:
					if score > score_other:
						score_other = score
		assert score_pref > score_other

	# Verify that |preferred_target| has a higher score then |other_target|
	# in the candidate list.
	def verify_expand_preferred_target(self, candidates, station, preferred_target, other_target):
		score1 = 0
		score2 = 0
		for c in candidates:
			if not c['action'] == "EXPAND":
				continue
			if c['station'] == station:
				if c['target'] == preferred_target:
					score1 = c['score']
				if c['target'] == other_target:
					score2 = c['score']
		assert score1 > score2

	# Chaining
	# All methods below this line can be chained.
	
	def init_customer_queue(self, ward1: str, ward2: str, ward3: str, ward4: str) -> "GameStateTester":
		self.gs.customer_queue = []
		for w in [ward1, ward2, ward3, ward4]:
			self.assert_ward(w)
			self.gs.customer_queue.append([w, []])
		return self
	
	def add_customer_to_queue(self, customer: str) -> "GameStateTester":
		self.assert_customer(customer)
		self.gs.add_customer_to_queue(customer)
		return self
		
	def init_player_hand(self, wards: list[str]) -> "GameStateTester":
		self.gs.players[self.player_id].add_to_hand(wards)
		return self
	
	def init_player_stores(self, stores: list[str]) -> "GameStateTester":
		player = self.gs.get_player(self.player_id)
		for s in stores:
			self.assert_store(s)
		player.reset_stores(stores)
		return self

	def open_store(self, station: str, store_type: str) -> "GameStateTester":
		self.assert_station(station)
		self.assert_store(store_type)
		self.gs.station_store[station] = (store_type, self.player_id)
		return self
	
	def open_opponent_store(self, station: str, store_type: str) -> "GameStateTester":
		self.assert_station(station)
		self.assert_store(store_type)
		self.gs.station_store[station] = (store_type, self.opponent_id)
		return self
	
	def add_customers_to_ward(self, ward: str, customers: list[str]) -> "GameStateTester":
		self.assert_ward(ward)
		for c in customers:
			self.assert_customer(c)
		self.gs.add_customers_to_ward(customers, ward)
		return self

	def add_track(self, station1: str, station2: str) -> "GameStateTester":
		self.assert_station(station1)
		self.assert_station(station2)
		self.gs.add_connection(station1, station2, self.player_id)
		return self

	def add_multiple_track(self, start_station: str, stations: list[str]) -> "GameStateTester":
		self.assert_station(start_station)
		for station in stations:
			self.assert_station(station)
			self.gs.add_connection(start_station, station, self.player_id)
		return self
	
	# Customer Queue
	
	def check_queue_customers(self, c1: list[str], c2: list[str], c3: list[str], c4: list[str]) -> "GameStateTester":
		qc = [c1, c2, c3, c4]
		for i in range(4):
			for c in qc[i]:
				self.assert_customer(c)
			self.verify_customers_match(qc[i], self.gs.customer_queue[i][1])
		return self

	# Open Store Action
	
	def check_open_preferred_location(self, preferred_station: str, other_stations: list[str]) -> "GameStateTester":
		num_candidates = len(other_stations)
		if preferred_station:
			num_candidates += 1

		c = self.open_gen.find_candidates(self.player_id)
		assert len(c) == num_candidates
		if preferred_station:
			self.assert_station(preferred_station)
			for s in other_stations:
				self.assert_station(preferred_station)
				self.verify_open_preferred_store_location(c, preferred_station, s)
		return self

	def check_open_preferred_type(self, station: str, store_type: str) -> "GameStateTester":
		c = self.open_gen.find_candidates(self.player_id)
		self.assert_station(station)
		self.assert_store(store_type)
		self.verify_open_preferred_store_type(c, station, store_type)
		return self

	# Expand Track Action
	
	def check_expand_from_station(self, start_station: str, preferred_station: str, other_stations: list[str]) -> "GameStateTester":
		self.assert_station(start_station)
		
		num_candidates = len(other_stations)
		if preferred_station:
			num_candidates += 1

		c = self.expand_gen.expand_from_stations(self.player_id)
		assert len(c) == num_candidates
		if preferred_station:
			self.assert_station(preferred_station)
			for other in other_stations:
				self.assert_station(other)
				self.verify_expand_preferred_target(c, start_station, preferred_station, other_stations)
		return self

	def check_expand_from_track(self, track_station: str, preferred_station: str, other_stations: list[str]) -> "GameStateTester":
		num_candidates = len(other_stations)
		if preferred_station:
			num_candidates += 1

		c = self.expand_gen.expand_from_track(self.player_id)
		assert len(c) == num_candidates
		if preferred_station:
			self.assert_station(preferred_station)
			for other in other_stations:
				self.assert_station(other)
				self.verify_expand_preferred_target(c, track_station, preferred_station, other_stations)
		return self
	
