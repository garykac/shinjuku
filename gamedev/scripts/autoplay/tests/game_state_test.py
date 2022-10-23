import pytest

from game_state_tester import GameStateTester

def test_queue_same():
	GameStateTester.newBuilder() \
		.init_customer_queue("Shinjuku", "Edogawa", "Setagaya", "Adachi") \
		.add_customer_to_queue("Food1") \
		.check_queue_customers(["Food1"], [], [], []) \
		\
		.add_customer_to_queue("Food2") \
		.check_queue_customers(["Food1", "Food2"], [], [], [])

def test_queue_different():
	GameStateTester.newBuilder() \
		.init_customer_queue("Shinjuku", "Edogawa", "Setagaya", "Adachi") \
		.add_customer_to_queue("Food1") \
		.check_queue_customers(["Food1"], [], [], []) \
		\
		.add_customer_to_queue("Books1") \
		.check_queue_customers(["Food1"], ["Books1"], [], []) \
		\
		.add_customer_to_queue("Clothing1") \
		.check_queue_customers(["Food1"], ["Books1"], ["Clothing1"], []) \
		\
		.add_customer_to_queue("Electronics1") \
		.check_queue_customers(["Food1"], ["Books1"], ["Clothing1"], ["Electronics1"])

def test_queue_grouping():
	GameStateTester.newBuilder() \
		.init_customer_queue("Shinjuku", "Edogawa", "Setagaya", "Adachi") \
		.add_customer_to_queue("Food1") \
		.add_customer_to_queue("Books1") \
		.add_customer_to_queue("Clothing1") \
		.add_customer_to_queue("Electronics2") \
		.check_queue_customers(["Food1"], ["Books1"], ["Clothing1"], ["Electronics2"]) \
		\
		.add_customer_to_queue("Books2") \
		.check_queue_customers(["Food1"], ["Books1", "Books2"], ["Clothing1"], ["Electronics2"]) \
		\
		.add_customer_to_queue("Food1") \
		.check_queue_customers(["Food1", "Food1"], ["Books1", "Books2"], ["Clothing1"], ["Electronics2"])
