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
from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

CARD_PNG_DIR = 'png'
CARD_PNG_BLEED_DIR = 'png-bleed'
CARD_SVG = 'ku-cards.svg'
CARD_BACK_SVG = 'tokyo-back.svg'
CARD_BACK_PNG = '_back.png'
# PrintPlayGames 18up
PPG_18UP_SVG = 'ppg-18up.svg'
PPG_18UP_DIR = 'ppg-18up'

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
# wards: Array of ward names
def export_ward_cards(dir, export_id, output_dirname, wards):
	src_svg = os.path.join(dir, CARD_SVG)

	outdir = os.path.join(dir, output_dirname)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	for w in wards:
		print(f"...{w}")
		out_png = os.path.join(outdir, f'{w}.png')
		export_card(src_svg, w, export_id, out_png)

def export_wards_png(dir, wards):
	print("Exporting png:")
	export_ward_cards(dir, 'card-export', CARD_PNG_DIR, wards)

def export_wards_png_bleed(dir, wards):
	print("Exporting png-bleed:")
	export_ward_cards(dir, 'card-export-bleed', CARD_PNG_BLEED_DIR, wards)

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
	actions.layerShow(name)
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
	src_svg = os.path.join(dir, f'pnp-9up-{type}.svg')
	out_pdf = os.path.join(dir, f'ku-cards-{type}.pdf')

	outdir = os.path.join(dir, f'pnp-9up-{type}-pdf')
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

print("Generating Shinjuku - Tokyo files...")
dir = os.getcwd()
export_cards(dir, TOKYO_WARDS)
export_card_backs(dir)
export_18up(dir)
export_9up(dir)
