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

def test_expand_station_prefer_connecting_to_another_ward():
	GameStateTester.newBuilder() \
		.open_store("Futako Tamagawa", "Food") \
		.check_expand_from_station("Futako Tamagawa", "Jiyugaoka", ["Sangenjaya"])

	GameStateTester.newBuilder() \
		.open_store("Shinagawa", "Food") \
		.check_expand_from_station("Shinagawa", "Meguro", ["Shimbashi", "Oimachi"])

def test_expand_station_prefer_ward_with_more_cards():
	GameStateTester.newBuilder() \
		.open_store("Todai Mae", "Food") \
		.check_expand_from_station("Todai Mae", "Iidabashi", ["Komagome"])

	GameStateTester.newBuilder() \
		.open_store("Iidabashi", "Food") \
		.add_track("Iidabashi", "Takadanobaba") \
		.check_expand_from_station("Iidabashi", "Shinjuku", ["Todai Mae", "Ueno", "Akihabara", "Tokyo"])

def test_expand_station_prefer_upgradable_station():
	GameStateTester.newBuilder() \
		.open_store("Hatchobori", "Food") \
		.check_expand_from_station("Hatchobori", "Tokyo", ["Mozen Nakacho"])

	GameStateTester.newBuilder() \
		.open_store("Shimbashi", "Food") \
		.check_expand_from_station("Shimbashi", "Tokyo", ["Roppongi", "Shinagawa", "Daiba", "Kachidoki"])

def test_expand_station_prefer_upgradable_station_over_ward_cards():
	GameStateTester.newBuilder() \
		.open_store("Oshiage", "Food") \
		.check_expand_from_station("Oshiage", "Ueno", ["Aoto", "Hirai", "Kinshicho"])

# Test expanding from track (that extends from a station)

def test_expand_track_dont_suggest_unavailable_connections():
	GameStateTester.newBuilder() \
		.open_store("Nerima", "Food") \
		.add_track("Nerima", "Nakano") \
		.add_multiple_track("Nakano", ["Takadanobaba", "Shinjuku", "Koenji"]) \
		.check_expand_from_track("Nakano", None, [])

def test_expand_track_dont_suggest_connecting_back_to_start_ward():
	GameStateTester.newBuilder() \
		.open_store("Shinjuku", "Food") \
		.add_track("Shinjuku", "Nakano") \
		.add_multiple_track("Nakano", ["Koenji", "Nerima"]) \
		.check_expand_from_track("Nakano", None, [])

def test_expand_track_prefer_connecting_to_another_ward():
	GameStateTester.newBuilder() \
		.open_store("Kachidoki", "Food") \
		.add_track("Kachidoki", "Shimbashi") \
		.check_expand_from_track("Shimbashi", "Tokyo", ["Roppongi", "Shinagawa", "Daiba"])

def test_expand_track_prefer_ward_with_more_cards():
	GameStateTester.newBuilder() \
		.open_store("Eifukucho", "Food") \
		.add_track("Eifukucho", "Meidai Mae") \
		.check_expand_from_track("Meidai Mae", "Shinjuku", ["Shibuya"])

	GameStateTester.newBuilder() \
		.open_store("Shin Kiba", "Food") \
		.add_track("Shin Kiba", "Mozen Nakacho") \
		.add_multiple_track("Mozen Nakacho", ["Hatchobori"]) \
		.check_expand_from_track("Mozen Nakacho", "Kachidoki", ["Kinshicho"])

def test_expand_track_prefer_upgradable_station():
	GameStateTester.newBuilder() \
		.open_store("Shinjuku", "Food") \
		.add_track("Shinjuku", "Iidabashi") \
		.add_multiple_track("Iidabashi", ["Takadanobaba"]) \
		.check_expand_from_track("Iidabashi", "Ueno", ["Todai Mae", "Akihabara", "Tokyo"])

def test_expand_track_prefer_upgradable_station_over_ward_cards():
	GameStateTester.newBuilder() \
		.open_store("Kinshicho", "Food") \
		.add_track("Kinshicho", "Oshiage") \
		.check_expand_from_track("Oshiage", "Ueno", ["Aoto", "Hirai"])

