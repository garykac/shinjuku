import random

from typing import Optional

from game_data import GameData
from logger import Logger
from player import Player

class GameState:
	def __init__(self, data: GameData, logger: Logger, log_options: dict[str,bool]) -> None:
		self.data = data
		self.logger: Logger = logger
		self.log_options = log_options

		self.ward_deck: list[str] = []
		self.ward_discard: list[str] = []
		self.ward_customers: dict[str, list] = {}
		self.station_store: dict[str, tuple[str,int]] = {}
		self.connections: dict[str, dict[str, int]] = {}
		self.upgrade_tokens: list[int] = []
		self.customer_bag: list[str] = []
		self.customer_queue: list = []
		self.players: list[Player] = []
		self.first_player: int = -1
		
		# Add neutral player.
		p = Player(self.data, self.logger, 0)
		self.players.append(p)
		
		self.enable_log = False
		# Add neutral track between Shinjuku and Yoyogi.
		self.add_connection("Shinjuku", "Yoyogi", 0)
		self.enable_log = True

	def log(self, msg: str) -> None:
		if self.enable_log:
			self.logger.log(msg)	

	def indent(self, n: int) -> None:
		self.logger.indent(n)

	def error(self, msg: str) -> None:
		self.logger.error(msg)

	def log_player_hand(self, player_id: int) -> None:
		player = self.get_player(player_id)
		self.log(f"Cards in hand: {player.get_hand()}")

	def log_player_components(self, player_id: int) -> None:
		player = self.get_player(player_id)
		self.log("Available components:")
		self.indent(1)
		stores = []
		total_stores = 0
		for t in self.data.CUSTOMER_TYPES:
			n = player.stores[t]
			if n != 0:
				total_stores += n
				if n == 1:
					stores.append(f"{t}")
				else:
					stores.append(f"{t} (x{n})")
		if total_stores == 0:
			store_desc = "None"
		else:
			store_desc = ', '.join(stores)
			
		self.log(f"Specialty stores: {store_desc}")
		self.log(f"Dept stores: {player.num_dept_stores}")
		self.log(f"Track: {player.num_track}")
		self.indent(-1)

	def log_player_customers(self, player_id: int) -> None:
		player = self.get_player(player_id)
		self.log("Customers obtained:")
		self.indent(1)
		
		for t in self.data.CUSTOMER_TYPES:
			count = sum(player.customers[t])
			cgraph = ['*-*' if x == 2 else '*' for x in player.customers[t]]
			self.log(f"{t:11} ({count:2}): {' '.join(cgraph)}")

		self.log(f"Score = {player.calc_score()}")

		self.indent(-1)

	def log_map_customers(self) -> None:
		self.log(f"Customers on map:")
		num_customers = 0
		self.indent(1)
		for ward in self.data.WARDS:
			customers = self.ward_customers[ward]
			if len(customers) != 0:
				self.log(f"{ward}: {' '.join(customers)}")
				num_customers += 1
		if num_customers == 0:
			self.log("None")		
		self.indent(-1)

	def log_map_stations(self) -> None:
		self.log(f"Stations with stores on map:")
		num_stations = 0
		self.indent(1)
		for station in self.data.station_wards:
			ward = self.data.station_wards[station]
			if station in self.station_store:
				(store_type, player_id) = self.station_store[station]
				self.log(f"{station} ({ward} ward): {store_type} (p{player_id})")
				num_stations += 1
		if num_stations == 0:
			self.log("None")		
		self.indent(-1)

	def log_map_connections(self) -> None:
		self.log(f"Track connections on map:")
		self.indent(1)
		for station in self.data.station_wards:
			if station in self.connections:
				info = []
				for target, owner in self.connections[station].items():
					info.append(f"{target}(p{owner})")
				self.log(station + " -> " + " ".join(info))
		self.indent(-1)

	def log_queue(self) -> None:
		index = 1
		self.log(f"Customer Queue:")
		self.indent(1)
		for q in self.customer_queue:
			(ward, customers) = q
			self.log(f"#{index}: {ward} {customers}")
			index += 1
		self.indent(-1)
	
	def log_ward_deck(self) -> None:
		self.log(f"Ward deck: [{','.join(self.ward_deck)}]")

	def log_discard_deck(self) -> None:
		self.log(f"Discard deck: [{','.join(self.ward_discard)}]")
		print(f"Discard deck: [{','.join(self.ward_discard)}]")

	#
	# Accessors
	#
	
	def get_first_player(self) -> int:
		return self.first_player

	def get_player(self, id: int) -> Player:
		return self.players[id]
	
	def get_ward_customers(self, ward: str) -> list[str]:
		if not ward in self.ward_customers:
			return []
		return self.ward_customers[ward]
	
	def get_station_info(self, station: str) -> tuple[str,int]:
		return self.station_store[station]

	#
	# Initialization
	#
	
	def init_ward_deck(self) -> None:
		if self.log_options['initial-setup']:
			self.log(f"Initialize ward deck:")
		for ward, count in self.data.ward_cards.items():
			for i in range(count):
				self.ward_deck.append(ward)
		random.shuffle(self.ward_deck)
		if self.log_options['initial-setup']:
			self.log_ward_deck()
		
	def init_customer_bag(self) -> None:
		for cinfo in self.data.customers:
			(type, weight, count) = cinfo
			for i in range(count):
				self.customer_bag.append(f"{type}{weight}")
		random.shuffle(self.customer_bag)
		if self.log_options['initial-setup']:
			self.log(f"Initialize customer bag:")
			self.log(f"[{','.join(self.customer_bag)}]")
		
	def init_customer_queue(self) -> None:
		self.log(f"Initializing customer queue:")
		self.indent(1)
		for i in range(4):
			w = self.draw_ward_card()
			self.customer_queue.append([w, []])

		for i in range(2):
			c = self.draw_customer()
			self.indent(1)
			self.add_customer_to_queue(c)
			self.indent(-1)
		self.indent(-1)
		self.log_queue()
		
	def init_gameboard(self) -> None:
		# Each ward is initially empty.
		for w in self.data.WARDS:
			self.ward_customers[w] = []
		
		# Initialize stack of upgrade tokens.
		self.upgrade_tokens = [3, 2, 2, 2, 1, 1]
	
	def add_seed_customers(self) -> None:
		self.log(f"Seed map with customers:")
		self.indent(1)
		seed_wards: list[str] = []
		while len(seed_wards) != 4:
			ward = self.draw_ward_card()
			self.indent(1)
			if ward in seed_wards:
				self.log(f"Duplicate ward card - discard and redraw")
				self.add_to_discard_pile(ward)
			else:
				seed_wards.append(ward)
				c1 = self.draw_customer()
				c2 = self.draw_customer()
				self.add_customers_to_ward([c1, c2], ward)
				self.add_to_discard_pile(ward)
			self.indent(-1)
		self.indent(-1)
		self.log_map_customers()

	def add_player(self) -> int:
		id = len(self.players)
		p = Player(self.data, self.logger, id)
		# The first player added becomes the first player.
		if self.first_player == -1:
			self.first_player = id
		self.players.append(p)
		return id

	#
	# Evaluate game state
	#
			
	def is_empty_station(self, station: str) -> bool:
		return not station in self.station_store

	def has_direct_connection(self, station1: str, station2: str) -> bool:
		if not station1 in self.connections:
			return False
		if not station2 in self.connections[station1]:
			return False
		return True

	def bonus_for_ward_customers(self, ward: str, store_type: str) -> int:
		customers = self.get_ward_customers(ward)
		bonus = 0
		# Find the best matching customer in the ward, taking into account
		# double customers.
		for c in customers:
			# For customer-store matching, only check the first char.
			if c[0] == store_type[0]:
				type_rank = self.data.customer_type_rank[c]
				if type_rank > bonus:
					bonus = type_rank
		return bonus

	def store_customer_match(self, store_type: str, customers: list[str]) -> Optional[str]:
		# Find the best matching customer in the ward, taking into account
		# double customers.
		bonus = 0
		matched_customer = None
		for c in customers:
			# For customer-store matching, only check the first char.
			if c[0] == store_type[0]:
				type_rank = self.data.customer_type_rank[c]
				if type_rank > bonus:
					bonus = type_rank
					matched_customer = c
		return matched_customer

	#
	# Update game state
	#
			
	def draw_ward_card(self, use_log=True) -> str:
		if len(self.ward_deck) == 0:
			# Reshuffle discard deck to create new draw deck.
			self.logger.log0("*** Reshuffling deck ***")
			self.ward_deck = self.ward_discard
			random.shuffle(self.ward_deck)
			self.ward_discard = []

		w = self.ward_deck.pop(0)
		if use_log:
			self.log(f"Draw {w} card from deck")
		return w
	
	def add_to_discard_pile(self, ward: str, use_log=True) -> None:
		self.ward_discard.append(ward)
		if use_log:
			self.log(f"Discard {ward} card")

	def draw_customer(self, use_log=True) -> Optional[str]:
		if len(self.customer_bag):
			c = self.customer_bag.pop(0)
			if use_log:
				self.log(f"Draw {c} from bag")
			return c
		return None

	def add_customer_to_queue(self, customer: Optional[str]) -> None:
		if customer is None:
			self.log(f"No customers in bag")
			return
		for q in self.customer_queue:
			(ward, customers) = q
			if (len(customers) == 0		# Empty queue slot
					# Compare first letter to see if customer type matches.
					or customers[0][0] == customer[0]
					):
				self.log(f"Add {customer} to queue on {ward}")
				customers.append(customer)
				return
	
	def add_customer_to_ward(self, customer: Optional[str], ward: str) -> None:
		if not ward in self.ward_customers:
			self.ward_customers[ward] = []
		self.ward_customers[ward].append(customer)
		self.log(f"Add {customer} customer to {ward}")
	
	def add_customers_to_ward(self, customers: list[Optional[str]], ward: str) -> None:
		if not ward in self.ward_customers:
			self.ward_customers[ward] = []
		for c in customers:
			self.ward_customers[ward].append(c)
		self.log(f"Add {customers} customers to {ward}")
	
	def place_customers_from_queue(self, player_id) -> int:
		self.log(f"Placing customers from queue:")
		self.indent(1)
		(ward, customers) = self.customer_queue.pop(0)
		self.add_customers_to_ward(customers, ward)
		self.players[player_id].add_to_hand([ward])
		self.indent(-1)
		return len(customers)

	def refresh_queue(self, num_customers: int) -> None:
		self.log(f"Refresh customer queue (with {num_customers} new customers):")
		self.indent(1)
		w = self.draw_ward_card()
		self.customer_queue.append([w, []])

		for i in range(num_customers):
			c = self.draw_customer()
			self.indent(1)
			self.add_customer_to_queue(c)
			self.indent(-1)
		self.indent(-1)

	def draw_hand(self, player_id: int) -> None:
		self.log(f"Draw hand for player {player_id}:")
		self.indent(1)
		wards = []
		for i in range(4):
			wards.append(self.draw_ward_card(False))
		self.players[player_id].add_to_hand(wards)
		self.indent(-1)

	def open_store_in_station(self, station: str, store_type: str, player_id: int) -> None:
		ward = self.data.station_wards[station]
		self.log(f"Open {store_type} store in {station} (in {ward})")
		if station in self.station_store:
			self.error(f"Station {station} already has a store")
		player = self.players[player_id]
		player.remove_store_from_supply(store_type)
		player.remove_from_hand(ward)
		self.add_to_discard_pile(ward)
		self.station_store[station] = (store_type, player_id)

	# Add one half of the connection: from |start| to |end|.
	def _add_connection(self, start: str, end: str, player_id) -> None:
		if not start in self.connections:
			self.connections[start] = {}
		self.connections[start][end] = player_id

	# Add a connection between |s1| and |s2|, owned by |player_id|.
	def add_connection(self, s1: str, s2: str, player_id:int) -> None:
		if not s1 in self.data.station_wards:
			self.error(f"Cannot add connection to invalid station {s1}")
		if not s2 in self.data.station_wards:
			self.error(f"Cannot add connection to invalid station {s2}")
		if not s2 in self.data.station_connections[s1]:
			self.error(f"Cannot add connection between {s1} and {s2}")
		self.players[player_id].remove_track_from_supply()
		self._add_connection(s1, s2, player_id)
		self._add_connection(s2, s1, player_id)
		ward1 = self.data.station_wards[s1]
		ward2 = self.data.station_wards[s2]
		self.log(f"Add track connecting {s1} (in {ward1}) and {s2} (in {ward2})")

	def draw_income(self, player_id: int) -> None:
		# Draw up to 4 cards, unless you already have 4 or more cards.
		hand = self.players[player_id].get_hand()
		num_draws = 1
		if len(hand) < 4:
			num_draws = 4 - len(hand)

		self.log(f"Draw income ({num_draws} cards) for player {player_id}:")
		self.indent(1)

		new_cards = []
		for i in range(num_draws):
			new_cards.append(self.draw_ward_card(False))
		self.players[player_id].add_to_hand(new_cards)
		self.indent(-1)

	def move_customers(self, ward: str, stations: list[str], player_id: int) -> None:
		self.log(f"Move customers in {ward}:")
		self.indent(1)
		customers = self.ward_customers[ward]
		for station in stations:
			if station in self.station_store:
				(store_type, owner_id) = self.station_store[station]
				c = self.store_customer_match(store_type, customers)
				if c:
					if owner_id == player_id:
						self.log(f"Visit {station} - Claim {c}")
					else:
						self.log(f"Visit {station} - Give {c} to player {owner_id}")
					customers.remove(c)
					self.get_player(owner_id).add_customer(c)
				else:
					self.log(f"Visit {station} - No matching customer")
			else:
				self.log(f"Visit {station} - No store")
		self.indent(-1)
	
