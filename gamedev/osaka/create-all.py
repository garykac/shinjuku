#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import os
import platform
import re
import subprocess
import sys

sys.path.append('../../../inkscape-lib')

from ghostscript import GhostScript
from imagemagick import ImageMagick
from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

MAIN_SVG = 'osaka.svg'
TEMP_PNG = '_temp.png'
# Ward Cards
CARD_DIR = 'cards'
CARD_PNG_DIR = os.path.join(CARD_DIR, 'png')
CARD_PNG_BLEED_DIR = os.path.join(CARD_DIR, 'png-bleed')
CARD_BACK_SVG = os.path.join(CARD_DIR, 'osaka-back.svg')
CARD_BACK_PNG = '_back.png'
# PrintPlayGames 18up
PPG_18UP_SVG = os.path.join(CARD_DIR, 'ppg-18up.svg')
PPG_18UP_DIR = os.path.join(CARD_DIR, 'ppg-18up')
# Map
MAP_PNG = 'osaka.png'

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

def export_card(svg, layer_id, export_id, width, height, png):
	actions = InkscapeActions()

	actions.layerShow("card-info-layer")
	actions.layerShow(layer_id)

	actions.exportFilename(png)
	#actions.exportDpi(300)
	actions.exportSize(width, height)
	actions.exportId(export_id)
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

# dir: Working directory
# export_id: Id of svg element to export
# width: width in pixels of output
# height: height in pixels of output
# output_dirname: Target dir where exported files will be written
# wards: Array of ward names
def export_ward_cards(dir, export_id, width, height, output_dirname, wards):
	src_svg = os.path.join(dir, MAIN_SVG)

	outdir = os.path.join(dir, output_dirname)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	temp_png = os.path.join(dir, TEMP_PNG)

	for w in wards:
		print(f"...{w}")
		# Export the card to have the correct width,height (in 300-dpi pixels) for the
		# card. Since the SVG doesn't have the file properly scaled for the card size
		# (because the map image is shared for the cards and board map) Inkscape will
		# automatically calculate the corresponding dpi based on the WxH, which we'll
		# have to correct afterwards to get a proper 300-dpi file of the right size.
		export_card(src_svg, f"card-{w}", export_id, width, height, temp_png)
		
		# Force dpi to be 300 (without scaling the image).
		ImageMagick.force_300_dpi(temp_png, os.path.join(outdir, f'{w}.png'))

	os.remove(temp_png)

def export_wards_png(dir, wards):
	print("Exporting png:")
	export_ward_cards(dir, 'card-export', 750, 1050, CARD_PNG_DIR, wards)

def export_wards_png_bleed(dir, wards):
	print("Exporting png-bleed:")
	export_ward_cards(dir, 'card-export-bleed', 822, 1122, CARD_PNG_BLEED_DIR, wards)

def export_cards(dir, wards):
	export_wards_png(dir, wards)
	export_wards_png_bleed(dir, wards)

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

def export_9up_page(svg, name, pdf):
	actions = InkscapeActions()
	actions.exportFilename(pdf)
	actions.layerShow(name)
	actions.exportDpi(300)
	actions.exportAreaPage()
	actions.exportTextToPath()
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

def combine_9up(dir, in_pdf_dir, out_pdf):
	out_pdf = os.path.join(dir, out_pdf)
	in_pdfs = []
	for pdf in [f'page{x:02}.pdf' for x in range(1,9)]:
		in_pdfs.append(os.path.join(dir, in_pdf_dir, pdf))
	GhostScript.combine_pdfs(out_pdf, in_pdfs)

def export_9up_type(dir, type):
	src_svg = os.path.join(dir, CARD_DIR, f'pnp-9up-{type}.svg')
	out_pdf = os.path.join(dir, CARD_DIR, f'osaka-cards-{type}.pdf')

	outdir = os.path.join(dir, CARD_DIR, f'pnp-9up-{type}-pdf')
	if not os.path.isdir(outdir):
		os.makedirs(outdir);
	
	print(f"Exporting pnp 9up ({type}):")
	pages = [f'page{x:02}' for x in range(1,9)]
	for page in ['_back', *pages]:
		print(f"...{page}")
		page_out_pdf = os.path.join(outdir, f'{page}.pdf')
		export_9up_page(src_svg, page, page_out_pdf)
	print("Combining 9up pages")
	combine_9up(dir, outdir, out_pdf)

def export_9up(dir):
	export_9up_type(dir, "letter")
	export_9up_type(dir, "a4")
	
def export_map_png(svg, png):
	actions = InkscapeActions()

	actions.layerShow("gameboard-outline")
	actions.layerShow("gameboard-title")
	actions.layerShow("station-labels")
	actions.layerShow("stations-overlay")
	actions.layerShow("stations")
	actions.layerShow("stations-underlay")
	actions.layerShow("connections")
	actions.layerShow("stations-shadow")
	actions.layerShow("ward-names")
	actions.layerShow("osaka-bay-label")
	actions.layerShow("ward-outlines")

	actions.exportFilename(png)
	actions.exportSize(6600, 6000)
	actions.exportId("gameboard-export")
	actions.exportDo()
	Inkscape.run_actions(svg, actions)

def export_map(dir):
	print("Exporting map...")
	svg = os.path.join(dir, MAIN_SVG)
	png = os.path.join(dir, MAP_PNG)
	temp_png = os.path.join(dir, TEMP_PNG)
	export_map_png(svg, temp_png)
	ImageMagick.force_300_dpi(temp_png, png)
	os.remove(temp_png)

print("Generating Shinjuku - Osaka files...")
dir = os.getcwd()
export_cards(dir, OSAKA_WARDS)
export_card_backs(dir)
export_18up(dir)
export_9up(dir)
export_map(dir)
