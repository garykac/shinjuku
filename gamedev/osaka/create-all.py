#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_card_generator import ShinjukuCardGenerator
from shinjuku_map_generator import ShinjukuMapGenerator

OSAKA_WARDS = [
	"abeno",
	"asahi",
	"chuo",
	"fukushima",
	"higashi-sumiyoshi",
	"higashi-yodogawa",
	"higashinari",
	"hirano",
	"ikuno",
	"joto",
	"kita",
	"konohana",
	"minato",
	"miyakojima",
	"naniwa",
	"nishi-yodogawa",
	"nishi",
	"nishinari",
	"suminoe",
	"sumiyoshi",
	"taisho",
	"tennoji",
	"tsurumi",
	"yodogawa",
]

OSAKA_WARD_CARD_COUNTS = {
	"abeno": 3,
	"asahi": 2,
	"chuo": 5,
	"fukushima": 2,
	"higashi-sumiyoshi": 3,
	"higashi-yodogawa": 4,
	"higashinari": 2,
	"hirano": 4,
	"ikuno": 4,
	"joto": 4,
	"kita": 5,
	"konohana": 2,
	"minato": 2,
	"miyakojima": 3,
	"naniwa": 2,
	"nishi-yodogawa": 2,
	"nishi": 3,
	"nishinari": 3,
	"suminoe": 3,
	"sumiyoshi": 4,
	"taisho": 2,
	"tennoji": 2,
	"tsurumi": 2,
	"yodogawa": 4,
}

options = {
	'card_svg': 'osaka.svg',
	'map_svg': 'osaka.svg',

	'wards': OSAKA_WARDS,
	'ward_counts': OSAKA_WARD_CARD_COUNTS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "osaka-cards",
	'card_back_svg': 'osaka-back.svg',
	'card_back_png': '_back.png',

	# Card layers
	'card_layers_common': ["card-info-layer"],
	'auto_card_layers': [ 'card-' ],
	
	# PrintPlayGames 18up
	'ppg_18up_dir': 'ppg-18up',

	# Map
	'map_dir': 'map',
	'map_png': 'osaka-map.png',
	'map_base_pdf': 'osaka-map',
	'map_landscape': True,
	'map_export': "gameboard-export",
	'map_layers': [
		"gameboard-outline",
		"gameboard-title",
		"station-labels",
		"stations-overlay",
		"stations",
		"stations-underlay",
		"connections",
		"stations-shadow",
		"ward-names",
		"osaka-bay-label",
		"ward-outlines",
	],
}

print("Generating Shinjuku - Osaka files...")
dir = os.getcwd()

def generate_cards(dir, options):
	cardgen = ShinjukuCardGenerator(dir, options)
	cardgen.export_cards()
	cardgen.export_card_backs()
	cardgen.export_18up()
	cardgen.export_9up()

def generate_map(dir, options):
	mapgen = ShinjukuMapGenerator(dir, options)
	mapgen.export_map()
	mapgen.export_split_pdf()

generate_cards(dir, options)
generate_map(dir, options)
