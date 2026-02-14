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

CARD_DIR = 'cards'
MAP_DIR = 'map'

options = {
	'card_svg': 'paris-cards.svg',
	'map_svg': 'paris-map.svg',
	'temp_png': '_temp.png',

	'wards': PARIS_ARRONDISSEMENTS,

	# Ward Cards
	'card_dir': CARD_DIR,
	'card_png_dir': os.path.join(CARD_DIR, 'png'),
	'card_png_bleed_dir': os.path.join(CARD_DIR, 'png-bleed'),
	'card_out_pdf_basename': "paris-cards",
	'card_back_svg': os.path.join(CARD_DIR, 'paris-back.svg'),
	'card_back_png': '_back.png',

	# Card layers
	'card_layers_common': ["card-info-layer"],
	'card_layers': {},
	
	# PrintPlayGames 18up
	'ppg_18up_svg': os.path.join(CARD_DIR, 'ppg-18up.svg'),
	'ppg_18up_dir': os.path.join(CARD_DIR, 'ppg-18up'),

	# Map
	'map_dir': MAP_DIR,
	'map_png': 'paris-map.png',
	'map_base_pdf': 'paris-map',
	'map_landscape': False,
	'map_export': "gameboard-export",
	'map_layers': [],
}

print("Generating Shinjuku - Paris files...")
dir = os.getcwd()

def generate_cards(dir, options):
	cardgen = ShinjukuCardGenerator(dir, options)
	cardgen.export_cards()
	cardgen.export_card_backs()
	cardgen.export_18up()

def generate_map(dir, options):
	mapgen = ShinjukuMapGenerator(options)
	mapgen.export_map(dir)
	mapgen.export_split_pdf(dir)

generate_cards(dir, options)
#generate_map(dir, options)
