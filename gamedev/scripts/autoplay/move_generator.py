from game_data import GameData
from game_state import GameState
from generator import CandidateGenerator
from logger import Logger

class MoveCustomerCandidateGenerator(CandidateGenerator):
	def __init__(self, data: GameData, gs: GameState, logger: Logger) -> None:
		self.data = data
		self.game_state = gs
		self.logger = logger

	def find_candidates(self, player_id: int) -> list[dict]:
		candidates = []
		candidates.extend(self.find_in_same_ward(player_id))
		return candidates

	def find_in_same_ward(self, player_id: int) -> list[dict]:
		gs = self.game_state
		player = gs.get_player(player_id)

		candidates = []
		for station, store_info in gs.station_store.items():
			(store_type, owner_id) = store_info
			ward = self.data.station_wards[station]
			if owner_id == player_id:
				if gs.bonus_for_ward_customers(ward, store_type) != 0:
					candidates.append({
						'action': "MOVE",
						'ward': ward,
						'cards': [ward],
						'stations': [station],
						'score': 20,
					})

		return candidates
