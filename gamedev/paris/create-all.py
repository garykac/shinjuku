#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import subprocess
import sys

sys.path.append('../../../inkscape-lib')

from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

CARD_DIR = 'cards'
CARD_PNG_DIR = os.path.join(CARD_DIR, 'png')
CARD_PNG_BLEED_DIR = os.path.join(CARD_DIR, 'png-bleed')
CARD_SVG = os.path.join(CARD_DIR, 'paris-cards.svg')
CARD_BACK_SVG = os.path.join(CARD_DIR, 'paris-back.svg')
CARD_BACK_PNG = '_back.png'
# PrintPlayGames 18up
PPG_18UP_SVG = os.path.join(CARD_DIR, 'ppg-18up.svg')
PPG_18UP_DIR = os.path.join(CARD_DIR, 'ppg-18up')
# Map
PARIS_MAP_SVG = 'paris.svg'
PARIS_MAP_PNG = 'paris.png'

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

def export_card(svg, layer_id, export_id, png):
	actions = InkscapeActions()

	actions.layerShow(layer_id)

	actions.exportFilename(png)
	actions.exportDpi(300)
	actions.exportId(export_id)
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

# dir: Working directory
# export_id: Id of svg element to export
# output_dirname: Target dir where exported files will be written
# arrs: Array of arrondissement names
def export_arrondissement_cards(dir, export_id, output_dirname, arrs):
	src_svg = os.path.join(dir, CARD_SVG)

	outdir = os.path.join(dir, output_dirname)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	for arr in arrs:
		print(f"...{arr}")
		out_png = os.path.join(outdir, f'{arr}.png')
		export_card(src_svg, arr, export_id, out_png)

def export_arrondissements_png(dir, arr):
	print("Exporting png:")
	export_arrondissement_cards(dir, 'card-export', CARD_PNG_DIR, arr)

def export_arrondissements_png_bleed(dir, arr):
	print("Exporting png-bleed:")
	export_arrondissement_cards(dir, 'card-export-bleed', CARD_PNG_BLEED_DIR, arr)

def export_cards(dir, arr):
	export_arrondissements_png(dir, arr)
	export_arrondissements_png_bleed(dir, arr)

def export_card_back(svg, export_id, png):
	actions = InkscapeActions()
	actions.exportFilename(png)
	actions.exportDpi(300)
	actions.exportId(export_id)
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

def export_card_backs(dir):
	print("Exporting card backs")
	svg = os.path.join(dir, CARD_BACK_SVG)
	export_card_back(svg, "export-rect", os.path.join(*[dir, CARD_PNG_DIR, CARD_BACK_PNG]))
	export_card_back(svg, "export-rect-bleed", os.path.join(*[dir, CARD_PNG_BLEED_DIR, CARD_BACK_PNG]))

def export_18up_page(svg, name, png):
	actions = InkscapeActions()
	actions.exportFilename(png)
	actions.layerShow(f"sheet-{name}")
	actions.exportDpi(300)
	actions.exportAreaPage()
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

def export_18up(dir):
	src_svg = os.path.join(dir, PPG_18UP_SVG)
	
	outdir = os.path.join(dir, PPG_18UP_DIR)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);
	
	print("Exporting ppg 18-up:")
	for page in ['_back', 'page01', 'page02', 'page03', 'page04']:
		print(f"...{page}")
		out_png = os.path.join(outdir, f'{page}.png')
		export_18up_page(src_svg, page, out_png)

def export_map_png(svg, png):
	actions = InkscapeActions()
	actions.exportFilename(png)
	actions.exportDpi(300)
	actions.exportId("gameboard-export")
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

def export_map(dir):
	print("Exporting map...")
	svg = os.path.join(dir, PARIS_MAP_SVG)
	png = os.path.join(dir, PARIS_MAP_PNG)
	export_map_png(svg, png)

print("Generating Shinjuku - Paris files...")
dir = os.getcwd()
export_cards(dir, PARIS_ARRONDISSEMENTS)
export_card_backs(dir)
export_18up(dir)
export_map(dir)
