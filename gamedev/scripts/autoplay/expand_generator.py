from game_data import GameData
from game_state import GameState
from generator import CandidateGenerator
from logger import Logger

class ExpandTrackCandidateGenerator(CandidateGenerator):
	def __init__(self, data: GameData, gs: GameState, logger: Logger) -> None:
		self.data = data
		self.game_state = gs
		self.logger = logger

	def find_candidates(self, player_id: int) -> list[dict]:
		gs = self.game_state
		player = gs.get_player(player_id)
		
		# Make sure player has at least one track available.
		if player.num_track == 0:
			return []
		
		candidates = []
		candidates.extend(self.expand_from_stations(player_id))
		candidates.extend(self.expand_from_track(player_id))
		return candidates
	
	# Single track expansions from the player's stores.
	def expand_from_stations(self, player_id: int) -> list[dict]:
		data = self.data
		gs = self.game_state
		player = gs.get_player(player_id)

		# Find all the stations that have stores owned by this player.
		candidates = []
		for station, store_info in gs.station_store.items():
			(store_type, owner) = store_info
			if owner == player_id:
				# Get all connections that involve this station.
				targets = data.station_connections[station]
				for target in targets:
					# Ignore connections that already have track.
					if (station in gs.connections
							and target in gs.connections[station]):
						continue
					score = 3
					# Connections that reach into a different ward.
					if data.station_wards[station] != data.station_wards[target]:
						# Bonus based on number of cards for ward.
						score += data.ward_cards[data.station_wards[target]]
						# Bonus for customers that match the store.
						score += gs.bonus_for_ward_customers(target, store_type)
					# Stations that can be upgraded to dept stores.
					if target in data.dept_store_stations:
						score += 6
					candidates.append({
						'action': "EXPAND",
						'station': station,
						'target': target,
						'score': score,
						})
		return candidates

	def expand_from_track(self, player_id: int) -> list[dict]:
		data = self.data
		gs = self.game_state
		player = gs.get_player(player_id)

		# Try to expand existing player track to reach customers.
		candidates = []
		all_tracks = gs.connections
		for stationA, connectA in all_tracks.items():
			# Look for following pattern:
			#   A-------B - - - C
			# A: store X owned by player
			# B: empty station
			# C: station in ward that contains customer X
			# Existing track between A-B
			# Empty connection between B-C 
			if not gs.is_empty_station(stationA):
				wardA = data.station_wards[stationA]
				(store_typeA, store_owner_idA) = gs.get_station_info(stationA)
				if store_owner_idA == player_id:
					# Player has a store on one side (A) of this track segment.
					# Try to expand from station on the other side (B) of this track.
					for stationB, track_owner_id in connectA.items():
						wardB = data.station_wards[stationB]
						if track_owner_id != player_id:
							continue
						if gs.is_empty_station(stationB):
							# Check all possible connections leading out of B.
							for stationC in data.station_connections[stationB]:
								# Ignore if there's already track between B and C.
								if gs.has_direct_connection(stationB, stationC):
									continue
								# Ignore if it connects back to the starting ward.
								wardC = data.station_wards[stationC]
								if wardA == wardC:
									continue
								score = 6
								# Downgrade connections to the same ward that the track
								# connects to.
								if wardB == wardC:
									score -= 3
								# Bonus based on number of cards for ward.
								score += data.ward_cards[wardC]
								# Connecting to ward with customers that match store in A.
								score += gs.bonus_for_ward_customers(wardC, store_typeA)
								# Stations that can be upgraded to dept stores.
								if stationC in data.dept_store_stations:
									score += 6
								candidates.append({
									'action': "EXPAND",
									'station': stationB,
									'target': stationC,
									'score': score,
									})
		return candidates

