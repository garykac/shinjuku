#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_generator import ShinjukuGenerator

PARIS_ARRONDISSEMENTS = [
	"01-louvre",
	"02-bourse",
	"03-temple",
	"04-hotel-de-ville",
	"05-pantheon",
	"06-luxembourg",
	"07-palais-bourbon",
	"08-elysee",
	"09-opera",
	"10-entrepot",
	"11-popincourt",
	"12-reuilly",
	"13-gobelins",
	"14-observatoire",
	"15-vaugirard",
	"16-passy",
	"17-batignolles-monceau",
	"18-butte-montmartre",
	"19-buttes-chaumont",
	"20-menilmontant",
]

PARIS_ARRONDISSEMENTS_CARD_COUNTS = {
	"01-louvre": 2,
	"02-bourse": 2,
	"03-temple": 2,
	"04-hotel-de-ville": 3,
	"05-pantheon": 3,
	"06-luxembourg": 2,
	"07-palais-bourbon": 3,
	"08-elysee": 3,
	"09-opera": 3,
	"10-entrepot": 3,
	"11-popincourt": 4,
	"12-reuilly": 4,
	"13-gobelins": 5,
	"14-observatoire": 4,
	"15-vaugirard": 5,
	"16-passy": 4,
	"17-batignolles-monceau": 5,
	"18-butte-montmartre": 5,
	"19-buttes-chaumont": 5,
	"20-menilmontant": 5,
}

PARIS_ARRONDISSEMENTS_CARD_COLORS = {
	"01-louvre": "green",
	"02-bourse": "yellow",
	"03-temple": "purple",
	"04-hotel-de-ville": "pink",
	"05-pantheon": "orange",
	"06-luxembourg": "purple",
	"07-palais-bourbon": "yellow",
	"08-elysee": "pink",
	"09-opera": "orange",
	"10-entrepot": "pink",
	"11-popincourt": "orange",
	"12-reuilly": "green",
	"13-gobelins": "purple",
	"14-observatoire": "pink",
	"15-vaugirard": "orange",
	"16-passy": "green",
	"17-batignolles-monceau": "yellow",
	"18-butte-montmartre": "purple",
	"19-buttes-chaumont": "green",
	"20-menilmontant": "yellow",
}

options = {
	'card_svg': 'paris-cards.svg',
	'map_svg': 'paris-map.svg',

	'wards': PARIS_ARRONDISSEMENTS,
	'ward_counts': PARIS_ARRONDISSEMENTS_CARD_COUNTS,
	'ward_colors': PARIS_ARRONDISSEMENTS_CARD_COLORS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "paris-cards",
	'card_back_svg': 'paris-back.svg',
	'card_back_png': '_back.png',

	'wards_with_dept_store': [
		"01-louvre", "04-hotel-de-ville", "07-palais-bourbon", "08-elysee", "09-opera",
		"10-entrepot", "12-reuilly", "13-gobelins", "14-observatoire",
	],
	
	# Card layers
	'auto_card_layers': [ 'card-', 'card-map-' ],
	'auto_card_layer_count': 'card-count-',
	'auto_card_layer_color': 'card-color-',
	
	# PrintPlayGames 18up
	'ppg_18up_dir': 'ppg-18up',

	# Map
	'map_dir': 'map',
	'map_png': 'paris-map.png',
	'map_base_pdf': 'paris-map',
	'map_landscape': False,
	'map_export': "gameboard-export",
}

print("Generating Shinjuku - Paris files...")
dir = os.getcwd()

gen = ShinjukuGenerator(dir, options)
gen.Generate()
