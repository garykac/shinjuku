import pytest

from game_state_tester import GameStateTester

def test_open():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Nerima", [])

def test_open_duplicate_cards():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima", "Nerima"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Nerima", [])

def test_open_occupied():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima"]) \
		.init_player_stores(["Food"]) \
		.open_opponent_store("Nerima", "Clothing") \
		.check_open_preferred_location(None, [])

def test_open_already_have_store_in_ward():
	# Don't propose Eifukucho since player already has a store in Suginami.
	GameStateTester.newBuilder() \
		.init_player_hand(["Suginami"]) \
		.init_player_stores(["Food"]) \
		.open_store("Koenji", "Clothing") \
		.check_open_preferred_location(None, [])

def test_open_prefer_ward_with_more_cards():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima", "Kita"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Nerima", ["Oji"])

	GameStateTester.newBuilder() \
		.init_player_hand(["Toshima", "Shinagawa"]) \
		.init_player_stores(["Food"]) \
		.open_opponent_store("Oimachi", "Clothing") \
		.open_opponent_store("Komagome", "Clothing") \
		.check_open_preferred_location("Meguro", ["Ikebukuro"])

def test_open_prefer_with_lots_of_connections():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima", "Nakano"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Nakano", ["Nerima"])

	GameStateTester.newBuilder() \
		.init_player_hand(["Koto"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Mozen Nakacho", ["Shin Kiba"])

	GameStateTester.newBuilder() \
		.init_player_hand(["Chiyoda", "Chuo"]) \
		.init_player_stores(["Food"]) \
		.open_opponent_store("Tokyo", "Clothing") \
		.open_opponent_store("Akihabara", "Clothing") \
		.check_open_preferred_location("Iidabashi", ["Hatchobori", "Kachidoki"])

def test_open_prefer_if_multiple_copies_in_hand():
	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima", "Itabashi", "Itabashi"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Oyama", ["Nerima"])

	GameStateTester.newBuilder() \
		.init_player_hand(["Nerima", "Nerima", "Itabashi"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Nerima", ["Oyama"])

def test_open_prefer_upgradable():
	GameStateTester.newBuilder() \
		.init_player_hand(["Meguro"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Naka Meguro", ["Jiyugaoka"])

	GameStateTester.newBuilder() \
		.init_player_hand(["Adachi", "Edogawa"]) \
		.init_player_stores(["Food"]) \
		.check_open_preferred_location("Kita Senju", ["Hirai", "Kasai Rinkai Koen"])

def test_open_matching_customer_in_ward():
	game = GameStateTester.newBuilder() \
		.init_player_hand(["Nerima"]) \
		.init_player_stores(["Food", "Clothing", "Books", "Electronics"]) \
		.add_customers_to_ward("Nerima", ["Books1"]) \
		.check_open_preferred_type("Nerima", "Books")

