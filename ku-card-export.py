#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto-generate cards from ku-cards.svg.
# All ward layers should be hidden before running this script since it will toggle
# the visibility of each one before rendering.

import os
import subprocess

from shutil import copyfile

# Tokyo Wards
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

# Paris Arrondissements
_arr = [
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

# svg: Name of svg file
# layer_object_name: Id of an object in the layer.
#    Note: Not the id of the layer.
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

def export_id(id, svg, png):
	subprocess.call([
		"/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
		"--file=%s" % os.path.abspath(os.path.join('', svg)),
		"--without-gui",
		
		"--export-png=%s" % os.path.abspath(os.path.join('', png)),
		"--export-dpi=300",
		"--export-text-to-path",
		"--export-id=%s" % id,
		])

def export_png(dir, basename, wards, id):
	
	src = os.path.join(dir, '%s.svg' % basename)
	cutline_svg = os.path.join(dir, '%s-cutline.svg' % basename)
	border_svg = os.path.join(dir, '%s-border.svg' % basename)
	ku_svg = os.path.join(dir, '%s-out.svg' % basename)

	# Create SVG file with card cutline.
	# If we're exporting the full card with bleed, then don't show cutline, just copy.
	copyfile(src, cutline_svg)
	if id == "cut-line":
		show_layer(cutline_svg, 'cut-line')

	# Create SVG file with Map Border.
	copyfile(cutline_svg, border_svg)	
	show_layer(border_svg, 'map-border-rect')

	outdir = os.path.join(dir, basename)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	for layer in wards:
		# Create SVG file with ku map.
		copyfile(border_svg, ku_svg)
		show_layer(ku_svg, '%s-title' % layer)

		# Export ku PNG.
		export_id(id, ku_svg, os.path.join(outdir, '%s.png' % layer))

	# Create SVG file for back (no map border).
	copyfile(cutline_svg, ku_svg)
	show_layer(ku_svg, 'card-back')
	export_id(id, ku_svg, os.path.join(outdir, 'back.png'))

	os.remove(ku_svg)
	os.remove(border_svg)
	os.remove(cutline_svg)
	

# Tokyo	
#export_png('.', 'ku-cards', _wards, "cut-line")
export_png('.', 'ku-cards-rounded', _wards, "cut-line")


# Paris
#export_png('paris', 'arr-cards', _arr, "cut-line")
#export_png('paris', 'arr-cards', _arr, "mpc-bbox")
