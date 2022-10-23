from game_data import GameData
from logger import Logger

class Player:
	def __init__(self, data: GameData, logger: Logger, id: int) -> None:
		self.data = data
		self.logger: Logger = logger
		
		self.id = id
		
		self.hand: list[str] = []

		self.stores: dict[str, int] = {}
		for t in self.data.CUSTOMER_TYPES:
			self.stores[t] = 2

		self.num_dept_stores: int = 3
		self.num_track: int = 16
		
		self.customers: dict[str, list[int]] = {}
		for t in self.data.CUSTOMER_TYPES:
			self.customers[t] = []

		# Initialize with 2 of each store type.
		stores = []		
		for t in self.data.CUSTOMER_TYPES:
			stores.append(t)
			stores.append(t)
		self.reset_stores(stores)

	def log(self, msg: str) -> None:
		self.logger.log(msg)	

	def indent(self, n: int) -> None:
		self.logger.indent(n)

	def error(self, msg: str) -> None:
		self.logger.error(msg)

	def reset_stores(self, stores) -> None:
		self.stores = {}
		for t in self.data.CUSTOMER_TYPES:
			self.stores[t] = 0
		for s in stores:
			self.add_store(s)

	def add_store(self, store_type) -> None:
		self.stores[store_type] += 1
			
	def get_hand(self) -> list[str]:
		return self.hand
	
	def add_to_hand(self, wards: list[str]) -> None:
		for w in wards:
			self.hand.append(w)
		self.log(f"Add {wards} to player {self.id}'s hand")

	def remove_from_hand(self, ward: str) -> None:
		if not ward in self.hand:
			self.error(f"Player does not have {ward} card in hand")
		self.hand.remove(ward)
		
	def remove_store_from_supply(self, store_type: str) -> None:
		if self.stores[store_type] < 1:
			self.error(f"Player does not have a {store_type} store available")
		self.stores[store_type] -= 1

	def remove_track_from_supply(self) -> None:
		if self.num_track < 1:
			self.error(f"Player does not have any track available")
		self.num_track -= 1

	def add_customer(self, customer) -> None:
		ctype = self.data.customer_2_type[customer]
		value = self.data.customer_2_value[customer]
		self.customers[ctype].append(value)

	def calc_score(self) -> int:
		score = 0
		base_count = 0
		counts = []
		for ctype, cvalues in self.customers.items():
			counts.append(sum(cvalues))

		set_score = self.data.customer_group_score.copy()
		for g in sorted(counts):
			score += (g - base_count) * set_score[0]
			base_count = g
			set_score.pop(0)
		return score
