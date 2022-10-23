from abc import ABC, abstractmethod

class CandidateGenerator(ABC):

	@abstractmethod
	def find_candidates(self, player_id: int) -> list[dict]:
		pass
