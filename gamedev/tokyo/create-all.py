#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_generator import ShinjukuGenerator

TOKYO_WARDS = [
	"01-chiyoda",
	"02-chuo",
	"03-minato",
	"04-shinjuku",
	"05-bunkyo",
	"06-taito",
	"07-sumida",
	"08-koto",
	"09-shinagawa",
	"10-meguro",
	"11-ota",
	"12-setagaya",
	"13-shibuya",
	"14-nakano",
	"15-suginami",
	"16-toshima",
	"17-kita",
	"18-arakawa",
	"19-itabashi",
	"20-nerima",
	"21-adachi",
	"22-katsushika",
	"23-edogawa",
]

TOKYO_WARD_CARD_COUNTS = {
	"01-chiyoda": 3,
	"02-chuo": 3,
	"03-minato": 4,
	"04-shinjuku": 4,
	"05-bunkyo": 2,
	"06-taito": 2,
	"07-sumida": 2,
	"08-koto": 3,
	"09-shinagawa": 3,
	"10-meguro": 2,
	"11-ota": 5,
	"12-setagaya": 5,
	"13-shibuya": 3,
	"14-nakano": 2,
	"15-suginami": 4,
	"16-toshima": 2,
	"17-kita": 2,
	"18-arakawa": 2,
	"19-itabashi": 4,
	"20-nerima": 4,
	"21-adachi": 4,
	"22-katsushika": 3,
	"23-edogawa": 4,
}

TOKYO_WARD_CARD_COLORS = {
	"01-chiyoda": "yellow",
	"02-chuo": "orange",
	"03-minato": "pink",
	"04-shinjuku": "green",
	"05-bunkyo": "orange",
	"06-taito": "green",
	"07-sumida": "purple",
	"08-koto": "yellow",
	"09-shinagawa": "purple",
	"10-meguro": "yellow",
	"11-ota": "green",
	"12-setagaya": "pink",
	"13-shibuya": "orange",
	"14-nakano": "yellow",
	"15-suginami": "purple",
	"16-toshima": "purple",
	"17-kita": "green",
	"18-arakawa": "pink",
	"19-itabashi": "pink",
	"20-nerima": "orange",
	"21-adachi": "yellow",
	"22-katsushika": "green",
	"23-edogawa": "orange",
}

options = {
	'card_svg': 'tokyo-cards.svg',
	'map_svg': 'tokyo-map.svg',

	'wards': TOKYO_WARDS,
	'ward_counts': TOKYO_WARD_CARD_COUNTS,
	'ward_colors': TOKYO_WARD_CARD_COLORS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "tokyo-cards",
	'card_back_svg': 'tokyo-back.svg',
	'card_back_png': '_back.png',

	'wards_with_dept_store': [
		"01-chiyoda", "03-minato", "04-shinjuku", "06-taito", "09-shinagawa", "10-meguro",
		"13-shibuya", "16-toshima", "21-adachi",
	],

	# Card layers
	'auto_card_layers': [ 'card-', 'card-map-' ],
	'auto_card_layer_count': 'card-count-',
	'auto_card_layer_color': 'card-color-',
	
	# Map
	'map_dir': 'map',
	'map_basename': 'tokyo-map',
	'map_landscape': False,
	'map_export': "gameboard-export",
}

print("Generating Shinjuku - Tokyo files...")
dir = os.getcwd()

gen = ShinjukuGenerator(dir, options)
gen.Generate()
