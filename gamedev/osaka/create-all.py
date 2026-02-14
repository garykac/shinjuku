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

CARD_DIR = 'cards'
MAP_DIR = 'map'

options = {
	'card_svg': 'osaka.svg',
	'map_svg': 'osaka.svg',
	'temp_png': '_temp.png',

	'wards': OSAKA_WARDS,

	# Ward Cards
	'card_dir': CARD_DIR,
	'card_png_dir': os.path.join(CARD_DIR, 'png'),
	'card_png_bleed_dir': os.path.join(CARD_DIR, 'png-bleed'),
	'card_out_pdf_basename': "osaka-cards",
	'card_back_svg': os.path.join(CARD_DIR, 'osaka-back.svg'),
	'card_back_png': '_back.png',

	# Card layers
	'card_layers_common': ["card-info-layer"],
	'card_layers': {},
	
	# PrintPlayGames 18up
	'ppg_18up_svg': os.path.join(CARD_DIR, 'ppg-18up.svg'),
	'ppg_18up_dir': os.path.join(CARD_DIR, 'ppg-18up'),

	# Map
	'map_dir': MAP_DIR,
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

cardgen = ShinjukuCardGenerator(options)
cardgen.export_cards(dir)
cardgen.export_card_backs(dir)
cardgen.export_18up(dir)
cardgen.export_9up(dir)

mapgen = ShinjukuMapGenerator(options)
mapgen.export_map(dir)
mapgen.export_split_pdf(dir)
