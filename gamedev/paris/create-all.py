#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../scripts')

from shinjuku_card_generator import ShinjukuCardGenerator
from shinjuku_map_generator import ShinjukuMapGenerator

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

options = {
	'card_svg': 'paris-cards.svg',
	'map_svg': 'paris-map.svg',

	'wards': PARIS_ARRONDISSEMENTS,
	'ward_counts': PARIS_ARRONDISSEMENTS_CARD_COUNTS,

	# Ward Cards
	'card_dir': 'cards',
	'card_png_dir': 'png',
	'card_png_bleed_dir': 'png-bleed',
	'card_out_pdf_basename': "paris-cards",
	'card_back_svg': 'paris-back.svg',
	'card_back_png': '_back.png',

	# Card layers
	'card_layers_common': ["card-info-layer"],
	'auto_card_layers': [ 'card-' ],
	
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

def generate_cards(dir, options):
	cardgen = ShinjukuCardGenerator(dir, options)
	cardgen.export_cards()
	cardgen.export_card_backs()
	cardgen.export_18up()

def generate_map(dir, options):
	mapgen = ShinjukuMapGenerator(dir, options)
	mapgen.export_map()
	mapgen.export_split_pdf()

generate_cards(dir, options)
generate_map(dir, options)
