import pytest

from game_state_tester import GameStateTester

# Test expanding around a station

def test_expand_station_dont_suggest_unavailable_connections():
	GameStateTester.newBuilder() \
		.open_store("Nerima", "Food") \
		.add_track("Nerima", "Nakano") \
		.check_expand_from_station("Nerima", None, [])

	GameStateTester.newBuilder() \
		.open_store("Ikebukuro", "Food") \
		.add_multiple_track("Ikebukuro", ["Oyama", "Komagome", "Takadanobaba"]) \
		.check_expand_from_station("Ikebukuro", None, [])

