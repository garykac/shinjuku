from game_data import GameData
from game_state import GameState
from generator import CandidateGenerator
from logger import Logger

class UpgradeStoreCandidateGenerator(CandidateGenerator):
	def __init__(self, data: GameData, gs: GameState, logger: Logger) -> None:
		self.data = data
		self.game_state = gs
		self.logger = logger

	def find_candidates(self, player_id: int) -> list[dict]:
		gs = self.game_state
		player = gs.get_player(player_id)
		return []
