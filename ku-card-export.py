#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto-generate cards from ku-cards.svg.
# All ward layers should be hidden before running this script since it will toggle
# their visibility before rendering.

import os
import subprocess

from shutil import copyfile

_wards = [
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

# 
# BUG: Only one layer can be toggled at a time, or none of them are.
def show_layer(svg, layer_object_name):
	subprocess.call([
		"/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
		"--file=%s" % os.path.abspath(os.path.join('', svg)),
		#"--without-gui",
		
		# Select object in layer (don't select the layer directly).
		"--select=%s" % layer_object_name,
		"--verb=LayerToggleHide",
		"--verb=UnhideAll",

		"--verb=FileSave",
		"--verb=FileQuit"
		])

def export_cut_line(svg, png):
	subprocess.call([
		"/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
		"--file=%s" % os.path.abspath(os.path.join('', svg)),
		"--without-gui",
		
		"--export-png=%s" % os.path.abspath(os.path.join('', png)),
		"--export-dpi=300",
		"--export-text-to-path",
		"--export-id=cut-line",
		])

def export_png():
	
	src = 'ku-cards.svg'
	cutline_svg = 'ku-cards-cutline.svg'
	border_svg = 'ku-cards-border.svg'
	ku_svg = 'ku-cards-out.svg'

	# Create SVG file with card cutline.
	copyfile(src, cutline_svg)	
	show_layer(cutline_svg, 'cut-line')

	# Create SVG file with Map Border.
	copyfile(cutline_svg, border_svg)	
	show_layer(border_svg, 'map-border-rect')

	outdir = "ku-cards"
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	for layer in _wards:
		# Create SVG file with ku map.
		copyfile(border_svg, ku_svg)
		show_layer(ku_svg, '%s-title' % layer)

		# Export ku PNG.
		export_cut_line(ku_svg, os.path.join(outdir, '%s.png' % layer))

	# Create SVG file for back (no map border).
	copyfile(cutline_svg, ku_svg)
	show_layer(ku_svg, 'ku-back')
	export_cut_line(ku_svg, os.path.join(outdir, 'back.png'))

	os.remove(ku_svg)
	os.remove(border_svg)
	os.remove(cutline_svg)
	
	
export_png()
