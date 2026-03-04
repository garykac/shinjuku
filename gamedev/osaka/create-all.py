#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_generator import ShinjukuGenerator

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

OSAKA_WARD_CARD_COLORS = {
	"abeno": "green",
	"asahi": "green",
	"chuo": "purple",
	"fukushima": "pink",
	"higashi-sumiyoshi": "pink",
	"higashi-yodogawa": "pink",
	"higashinari": "green",
	"hirano": "purple",
	"ikuno": "yellow",
	"joto": "orange",
	"kita": "orange",
	"konohana": "yellow",
	"minato": "purple",
	"miyakojima": "yellow",
	"naniwa": "pink",
	"nishi-yodogawa": "green",
	"nishi": "green",
	"nishinari": "yellow",
	"suminoe": "pink",
	"sumiyoshi": "orange",
	"taisho": "orange",
	"tennoji": "orange",
	"tsurumi": "purple",
	"yodogawa": "purple",
}

options = {
	'card_svg': 'osaka-cards.svg',
	'map_svg': 'osaka-map.svg',

	'wards': OSAKA_WARDS,
	'ward_counts': OSAKA_WARD_CARD_COUNTS,
	'ward_colors': OSAKA_WARD_CARD_COLORS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "osaka-cards",
	'card_back_svg': 'osaka-back.svg',
	'card_back_png': '_back.png',

	'wards_with_dept_store': [
		"abeno", "chuo", "ikuno", "kita", "konohana", "minato", "miyakojima", "naniwa",
		"nishinari", "tennoji", "yodogawa",
	],

	# Card layers
	'auto_card_layers': [ 'card-', 'card-map-' ],
	'auto_card_layer_count': 'card-count-',
	'auto_card_layer_color': 'card-color-',
	
	# Map
	'map_dir': 'map',
	'map_basename': 'osaka-map',
	'map_landscape': True,
	'map_export': "gameboard-export",
}

print("Generating Shinjuku - Osaka files...")
dir = os.getcwd()

gen = ShinjukuGenerator(dir, options)
gen.Generate()
