class GameData:
	def __init__(self) -> None:
		self.ward_cards: dict[str, int] = {}
		self.wards_adjacent: dict[str, list[str]] = {}
		self.station_wards: dict[str, str] = {}
		self.station_connections: dict[str, list[str]] = {}
		self.dept_store_stations: list[str] = []
		self.customers: list[list] = []
		self.customer_type_rank: dict[str, int] = {}
		self.customer_group_score: list[int] = []
		self.init_data()
		self.validate_data()
		
		self.ward_stations: dict[str, list[str]] = {}
		
		self.build_data()

	def init_data(self) -> None:
		self.WARDS = [
			"Chiyoda",
			"Chuo",
			"Minato",
			"Shinjuku",
			"Bunkyo",
			"Taito",
			"Sumida",
			"Koto",
			"Shinagawa",
			"Meguro",
			"Ota",
			"Setagaya",
			"Shibuya",
			"Nakano",
			"Suginami",
			"Toshima",
			"Kita",
			"Arakawa",
			"Itabashi",
			"Nerima",
			"Adachi",
			"Katsushika",
			"Edogawa",
		]

		self.CUSTOMER_TYPES = [
			"Food", "Clothing", "Books", "Electronics",
		]

		# Number of cards for each ward.
		self.ward_cards = {
			"Chiyoda": 3,
			"Chuo": 3,
			"Minato": 4,
			"Shinjuku": 4,
			"Bunkyo": 2,
			"Taito": 2,
			"Sumida": 2,
			"Koto": 3,
			"Shinagawa": 3,
			"Meguro": 2,
			"Ota": 5,
			"Setagaya": 5,
			"Shibuya": 3,
			"Nakano": 2,
			"Suginami": 4,
			"Toshima": 2,
			"Kita": 2,
			"Arakawa": 2,
			"Itabashi": 4,
			"Nerima": 4,
			"Adachi": 4,
			"Katsushika": 3,
			"Edogawa": 4,
		}

		self.wards_adjacent = {
			"Chiyoda": ["Bunkyo", "Taito", "Chuo", "Minato", "Shinjuku"],
			"Chuo": ["Taito", "Sumida", "Koto", "Minato", "Chiyoda"],
			"Minato": ["Shinjuku", "Chiyoda", "Chuo", "Koto", "Shinagawa", "Shibuya"],
			"Shinjuku": ["Toshima", "Bunkyo", "Chiyoda", "Minato", "Shibuya", "Nakano"],
			"Bunkyo": ["Toshima", "Kita", "Arakawa", "Taito", "Chiyoda", "Shinjuku"],
			"Taito": ["Arakawa", "Sumida", "Chuo", "Chiyoda", "Bunkyo"],
			"Sumida": ["Adachi", "Katsushika", "Edogawa", "Koto", "Chuo", "Taito", "Arakawa"],
			"Koto": ["Sumida", "Edogawa", "Ota", "Shinagawa", "Minato", "Chuo"],
			"Shinagawa": ["Minato", "Koto", "Ota", "Meguro", "Shibuya"],
			"Meguro": ["Shibuya", "Shinagawa", "Ota", "Setagaya"],
			"Ota": ["Shinagawa", "Koto", "Setagaya", "Meguro"],
			"Setagaya": ["Suginami", "Shibuya", "Meguro", "Ota"],
			"Shibuya": ["Nakano", "Shinjuku", "Minato", "Shinagawa", "Meguro", "Setagaya", "Suginami"],
			"Nakano": ["Nerima", "Toshima", "Shinjuku", "Shibuya", "Suginami"],
			"Suginami": ["Nerima", "Nakano", "Shibuya", "Setagaya"],
			"Toshima": ["Itabashi", "Kita", "Bunkyo", "Shinjuku", "Nakano", "Nerima"],
			"Kita": ["Adachi", "Arakawa", "Bunkyo", "Toshima", "Itabashi"],
			"Arakawa": ["Adachi", "Sumida", "Taito", "Bunkyo", "Kita"],
			"Itabashi": ["Kita", "Toshima", "Nerima"],
			"Nerima": ["Itabashi", "Toshima", "Nakano", "Suginami"],
			"Adachi": ["Katsushika", "Sumida", "Arakawa", "Kita"],
			"Katsushika": ["Edogawa", "Sumida", "Adachi"],
			"Edogawa": ["Katsushika", "Sumida", "Koto"],
		}

		self.station_wards = {
			"Tokyo": "Chiyoda",
			"Akihabara": "Chiyoda",
			"Iidabashi": "Chiyoda",
			"Hatchobori": "Chuo",
			"Kachidoki": "Chuo",
			"Shimbashi": "Minato",
			"Roppongi": "Minato",
			"Shinagawa": "Minato",
			"Daiba": "Minato",
			"Shinjuku": "Shinjuku",
			"Takadanobaba": "Shinjuku",
			"Yotsuya": "Shinjuku",
			"Todai Mae": "Bunkyo",
			"Ueno": "Taito",
			"Oshiage": "Sumida",
			"Kinshicho": "Sumida",
			"Mozen Nakacho": "Koto",
			"Shin Kiba": "Koto",
			"Meguro": "Shinagawa",
			"Oimachi": "Shinagawa",
			"Naka Meguro": "Meguro",
			"Jiyugaoka": "Meguro",
			"Omori": "Ota",
			"Tamagawa": "Ota",
			"Meidai Mae": "Setagaya",
			"Sangenjaya": "Setagaya",
			"Futako Tamagawa": "Setagaya",
			"Shibuya": "Shibuya",
			"Yoyogi": "Shibuya",
			"Ebisu": "Shibuya",
			"Nakano": "Nakano",
			"Koenji": "Suginami",
			"Eifukucho": "Suginami",
			"Ikebukuro": "Toshima",
			"Komagome": "Toshima",
			"Oji": "Kita",
			"Nishi Nippori": "Arakawa",
			"Oyama": "Itabashi",
			"Nerima": "Nerima",
			"Kita Senju": "Adachi",
			"Aoto": "Katsushika",
			"Shin Koiwa": "Katsushika",
			"Hirai": "Edogawa",
			"Kasai Rinkai Koen": "Edogawa",
		}

		self.station_connections = {
			# Chiyoda
			"Tokyo": ["Akihabara", "Hatchobori", "Shimbashi", "Yotsuya", "Iidabashi"],
			"Akihabara": ["Ueno", "Kinshicho", "Tokyo", "Iidabashi"],
			"Iidabashi": ["Todai Mae", "Ueno", "Akihabara", "Tokyo", "Shinjuku", "Takadanobaba"],
			# Chuo
			"Hatchobori": ["Mozen Nakacho", "Tokyo"],
			"Kachidoki": ["Mozen Nakacho", "Shimbashi"],
			# Minato
			"Shimbashi": ["Tokyo", "Kachidoki", "Daiba", "Shinagawa", "Roppongi"],
			"Roppongi": ["Shimbashi", "Ebisu", "Yoyogi", "Yotsuya"],
			"Shinagawa": ["Shimbashi", "Oimachi", "Meguro"],
			"Daiba": ["Shin Kiba", "Oimachi", "Shimbashi"],
			# Shinjuku
			"Shinjuku": ["Takadanobaba", "Iidabashi", "Yotsuya", "Yoyogi", "Meidai Mae", "Nakano"],
			"Takadanobaba": ["Ikebukuro", "Iidabashi", "Shinjuku", "Nakano"],
			"Yotsuya": ["Tokyo", "Roppongi", "Shinjuku"],
			# Bunkyo
			"Todai Mae": ["Iidabashi", "Komagome"],
			# Taito
			"Ueno": ["Kita Senju", "Oshiage", "Akihabara", "Iidabashi", "Nishi Nippori"],
			# Sumida
			"Oshiage": ["Aoto", "Hirai", "Kinshicho", "Ueno"],
			"Kinshicho": ["Oshiage", "Hirai", "Mozen Nakacho", "Akihabara"],
			# Koto
			"Mozen Nakacho": ["Kinshicho", "Shin Kiba", "Kachidoki", "Hatchobori"],
			"Shin Kiba": ["Kasai Rinkai Koen", "Daiba", "Mozen Nakacho"],
			# Shinagawa
			"Meguro": ["Shinagawa", "Oimachi", "Ebisu"],
			"Oimachi": ["Shinagawa", "Daiba", "Omori", "Jiyugaoka", "Meguro"],
			# Meguro
			"Naka Meguro": ["Shibuya", "Ebisu", "Jiyugaoka"],
			"Jiyugaoka": ["Naka Meguro", "Oimachi", "Tamagawa", "Futako Tamagawa"],
			# Ota
			"Omori": ["Oimachi"],
			"Tamagawa": ["Jiyugaoka"],
			# Setagaya
			"Meidai Mae": ["Shinjuku", "Shibuya", "Eifukucho"],
			"Sangenjaya": ["Shibuya", "Futako Tamagawa"],
			"Futako Tamagawa": ["Sangenjaya", "Jiyugaoka"],
			# Shibuya
			"Shibuya": ["Yoyogi", "Ebisu", "Naka Meguro", "Sangenjaya", "Meidai Mae"],
			"Yoyogi": ["Roppongi", "Shibuya", "Shinjuku"],
			"Ebisu": ["Roppongi", "Meguro", "Naka Meguro", "Shibuya"],
			# Nakano
			"Nakano": ["Takadanobaba", "Shinjuku", "Koenji", "Nerima"],
			# Suginami
			"Koenji": ["Nakano"],
			"Eifukucho": ["Meidai Mae"],
			# Toshima
			"Ikebukuro": ["Komagome", "Takadanobaba", "Oyama"],
			"Komagome": ["Oji", "Nishi Nippori", "Todai Mae", "Ikebukuro"],
			# Kita
			"Oji": ["Nishi Nippori", "Komagome"],
			# Arakawa
			"Nishi Nippori": ["Kita Senju", "Ueno", "Komagome", "Oji"],
			# Itabashi
			"Oyama": ["Ikebukuro"],
			# Nerima
			"Nerima": ["Nakano"],
			# Adachi
			"Kita Senju": ["Aoto", "Ueno", "Nishi Nippori"],
			# Katsushika
			"Aoto": ["Oshiage", "Kita Senju"],
			"Shin Koiwa": ["Hirai"],
			# Edogawa
			"Hirai": ["Shin Koiwa", "Kinshicho", "Oshiage"],
			"Kasai Rinkai Koen": ["Shin Kiba"],
		}

		self.dept_store_stations = [
			# Chiyoda
			"Tokyo",
			"Akihabara",
			# Chuo - none
			# Minato
			"Shimbashi",
			"Shinagawa",
			# Shinjuku
			"Shinjuku",
			"Takadanobaba",
			# Bunkyo - none
			# Taito
			"Ueno",
			# Sumida - none
			# Koto - none
			# Shinagawa
			"Meguro",
			# Meguro
			"Naka Meguro",
			# Ota - none
			# Setagaya - none
			# Shibuya
			"Shibuya",
			# Nakano - none
			# Suginami - none
			# Toshima
			"Ikebukuro",
			# Kita - none
			# Arakawa - none
			# Itabashi - none
			# Nerima - none
			# Adachi
			"Kita Senju",
			# Katsushika - none
			# Edogawa - none
		]
				
		self.customers = [
			["Food", 1, 22],
			["Food", 2, 1],
			["Clothing", 1, 16],
			["Clothing", 2, 4],
			["Books", 1, 8],
			["Books", 2, 8],
			["Electronics", 1, 2],
			["Electronics", 2, 11],
		]

		self.customer_type_rank = {
			"Food1": 8,
			"Food2": 10,
			"Clothing1": 9,
			"Clothing2": 11,
			"Books1": 10,
			"Books2": 12,
			"Electronics1": 11,
			"Electronics2": 13,
		}
		
		self.customer_2_type = {
			"Food1": "Food",
			"Food2": "Food",
			"Clothing1": "Clothing",
			"Clothing2": "Clothing",
			"Books1": "Books",
			"Books2": "Books",
			"Electronics1": "Electronics",
			"Electronics2": "Electronics",
		}
		
		self.customer_2_value = {
			"Food1": 1,
			"Food2": 2,
			"Clothing1": 1,
			"Clothing2": 2,
			"Books1": 1,
			"Books2": 2,
			"Electronics1": 1,
			"Electronics2": 2,
		}
		
		self.customer_group_score = [10, 6, 3, 1]

	def validate_data(self) -> None:
		# Validate card data.
		card_count: int = 0
		for w, count in self.ward_cards.items():
			card_count += count
		if card_count != 72:
			print("Incorrect number of ward cards in deck :", card_count, "instead of 72")

		# Validate map data (wards, ward adjacency, stations, station connections,
		# dept store locations).
		for w in self.WARDS:
			for aw in self.wards_adjacent[w]:
				if not aw in self.WARDS:
					print("Invalid ward :", aw)
				if not w in self.wards_adjacent[aw]:
					print("Missing ward :", w, "in wards adjacent to", aw)
		for s, w in self.station_wards.items():
			if not w in self.WARDS:
				print("Invalid ward :", w, "for station", s)
		for s, connections in self.station_connections.items():
			for c in connections:
				if not c in self.station_wards:
					print("Invalid station :", c, "for connections from", s)
				if not s in self.station_connections[c]:
					print("Missing station :", s, "in connections from", c)
		for s in self.dept_store_stations:
			if not s in self.station_connections:
				print("Invalid station :", s, "in dept store station list")

		# Validate customer data.				
		ccount = {}
		cweight = {}
		for t in self.CUSTOMER_TYPES:
			ccount[t] = 0
			cweight[t] = 0
		total_count = 0
		for cinfo in self.customers:
			(type, weight, count) = cinfo
			ccount[type] += count
			cweight[type] += weight * count
			total_count += count
		if total_count != 72:
			print("Invalid customer count :", total_count, "(expected 72))")
		for t in self.CUSTOMER_TYPES:
			if cweight[t] != 24:
				print("Invalid customer type balance for", t, ":", cweight[t], "(expected 24))")

	def build_data(self) -> None:
		# Create list of stations for each ward.
		for w in self.WARDS:
			self.ward_stations[w] = []
		for s, w in self.station_wards.items():
			self.ward_stations[w].append(s)
		
