#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_generator import ShinjukuGenerator

SEOUL_WARDS = [
	"dobong",
	"dongdaemun",
	"dongjak",
	"eunpyeong",
	"gangbuk",
	"gangdong",
	"gangnam",
	"gangseo",
	"geumcheon",
	"guro",
	"gwanak",
	"gwangjin",
	"jongno",
	"jung",
	"jungnang",
	"mapo",
	"nowon",
	"seocho",
	"seodaemun",
	"seongbuk",
	"seongdong",
	"songpa",
	"yangcheon",
	"yeongdeungpo",
	"yongsan",
]

SEOUL_WARD_CARD_COUNTS = {
	"dobong": 2,
	"dongdaemun": 3,
	"dongjak": 3,
	"eunpyeong": 3,
	"gangbuk": 2,
	"gangdong": 3,
	"gangnam": 4,
	"gangseo": 4,
	"geumcheon": 2,
	"guro": 3,
	"gwanak": 4,
	"gwangjin": 3,
	"jongno": 2,
	"jung": 2,
	"jungnang": 3,
	"mapo": 3,
	"nowon": 4,
	"seocho": 3,
	"seodaemun": 2,
	"seongbuk": 3,
	"seongdong": 2,
	"songpa": 4,
	"yangcheon": 3,
	"yeongdeungpo": 3,
	"yongsan": 2,
}

SEOUL_WARD_CARD_COLORS = {
	"dobong": "green",
	"dongdaemun": "green",
	"dongjak": "orange",
	"eunpyeong": "orange",
	"gangbuk": "yellow",
	"gangdong": "purple",
	"gangnam": "green",
	"gangseo": "pink",
	"geumcheon": "pink",
	"guro": "yellow",
	"gwanak": "purple",
	"gwangjin": "pink",
	"jongno": "pink",
	"jung": "orange",
	"jungnang": "orange",
	"mapo": "yellow",
	"nowon": "pink",
	"seocho": "yellow",
	"seodaemun": "green",
	"seongbuk": "purple",
	"seongdong": "yellow",
	"songpa": "orange",
	"yangcheon": "purple",
	"yeongdeungpo": "green",
	"yongsan": "purple",
}

options = {
	'card_svg': 'seoul-cards.svg',
	'map_svg': 'seoul-map.svg',

	'wards': SEOUL_WARDS,
	'ward_counts': SEOUL_WARD_CARD_COUNTS,
	'ward_colors': SEOUL_WARD_CARD_COLORS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "seoul-cards",
	'card_back_svg': 'seoul-back.svg',
	'card_back_png': '_back.png',

	'wards_with_dept_store': [
		"gangnam", "guro", "gwanak", "gwangjin", "jung", "mapo", "seocho", "seongdong", "songpa",
	],
	
	# Card layers
	'auto_card_layers': [ 'card-', 'card-map-' ],
	'auto_card_layer_count': 'card-count-',
	'auto_card_layer_color': 'card-color-',
	
	# Map
	'map_dir': 'map',
	'map_png': 'seoul-map.png',
	'map_base_pdf': 'seoul-map',
	'map_landscape': True,
	'map_export': "gameboard-export",
}

print("Generating Shinjuku - Seoul files...")
dir = os.getcwd()

gen = ShinjukuGenerator(dir, options)
gen.Generate()
