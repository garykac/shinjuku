#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto-generate cards from ku-cards.svg.
#
# All ward layers should be hidden before running this script since it will toggle
# the visibility of each one before rendering.
#
# The "Map border" and "Cut" layers should be hidden. They will be made visible
# if necessary.

# Each svg file should be structured as follows:
# * Layer "Cut 2.5 x 3.5" (with outline of 2.5x3.5 card)
#   * Rect id = "cut-line"
# * Layer "Map border" (black map outline)
#   * Rect id = "map-border-rect"
#
# For each ward:
# * Layer with name given in array (e.g.: "01-chiyoda")
#   * Item with id = layer_name + "_title" (e.g.: "01-chiyoda-title")
# The "map-border-rect" will automatically be shown for each ward card.
#
# For card back (if present):
# * Layer "Card back"
#   * Rect id = "card-back"
#
# For exporting:
# * Layer "Size 2.74 x 3.74 MPC" (MPC export layer)
#   * Rect id = "mpc-bbox"
#
# Note that the layer names are not required, but the svg ids must be set correctly.

# To export:
# * Cards for use in documentation, export id = "cut-line"
# * Cards for sending to be printed, export id = "mpc-bbox"

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

# London boroughs (subset that appear in the game)
_london = [
	"barnet",
	"brent",
	"camden",
	"city",  # Not really a borough
	"greenwich",
	"hackney",
	"hammersmith",
	"haringsey",
	"islington",
	"kensington",
	"lambeth",
	"lewisham",
	"newham",
	"southwark",
	"tower-hamlets",
	"waltham-forest",
	"wandsworth",
	"westminster",
]

# svg: Name of svg file
# layer_object_name: Id of an object in the layer.
#    Note: Not the id of the layer.
# BUG: Only one layer can be toggled at a time, or none of them are.
def show_layer(svg, layer_object_name):
	subprocess.call([
		"/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
		"--file=%s" % os.path.abspath(os.path.join('', svg)),
		#"--without-gui",  # Inkscape crashes when this is set here.
		
		# Select object in layer (don't select the layer directly).
		"--select=%s" % layer_object_name,
		"--verb=LayerToggleHide",
		"--verb=UnhideAll",

		"--verb=FileSave",
		"--verb=FileQuit"
		])

def svg_export_id(id, svg, png):
	subprocess.call([
		"/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
		"--file=%s" % os.path.abspath(os.path.join('', svg)),
		"--without-gui",
		
		"--export-png=%s" % os.path.abspath(os.path.join('', png)),
		"--export-dpi=300",
		"--export-text-to-path",
		"--export-id=%s" % id,
		])

# dir: Working directory
# basename: Target dir where exported files will be written
# wards: Array of base filenames
# export_id: The svg id to export for each card
#     Note: Layer ids cannot be exported, so this must be an object in the layer.
# has_back: Does the file include a card back image?
def export_png(dir, basename, wards, export_id, has_back):
	
	src = os.path.join(dir, '%s.svg' % basename)
	cutline_svg = os.path.join(dir, '%s-cutline.svg' % basename)
	border_svg = os.path.join(dir, '%s-border.svg' % basename)
	ku_svg = os.path.join(dir, '%s-out.svg' % basename)

	# Create SVG file with card cutline.
	# If we're exporting the full card with bleed, then don't show cutline, just make
	# a copy of the file for the next stage.
	copyfile(src, cutline_svg)
	if export_id == "cut-line":
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
		svg_export_id(export_id, ku_svg, os.path.join(outdir, '%s.png' % layer))

	if has_back:
		# Create SVG file for back (no map border).
		copyfile(cutline_svg, ku_svg)
		show_layer(ku_svg, 'card-back')
		svg_export_id(export_id, ku_svg, os.path.join(outdir, 'back.png'))

	os.remove(ku_svg)
	os.remove(border_svg)
	os.remove(cutline_svg)
	

# Tokyo	
#export_png('.', 'ku-cards', _wards, "cut-line", True)
# Cards with transparent rounded border (for documentation).
#export_png('.', 'ku-cards-rounded', _wards, "cut-line", True)

# Paris
#export_png('paris', 'arr-cards', _arr, "cut-line", False)
#export_png('paris', 'arr-cards', _arr, "mpc-bbox", False)

# London
export_png('london', 'london-cards', _london, "mpc-bbox", False)
