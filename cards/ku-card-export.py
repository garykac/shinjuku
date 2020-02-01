#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto-generate card images from ku-cards.svg.
#
# Before running this script, make sure the SVG file has layers hidden as follows:
#
# * All top level layers should be HIDDEN *except* for the three layer grouls:
#   "B&W", "Clip" and "Bleed"
# * Within the "B&W", "Clip" and "Bleed" groups, all layers should be HIDDEN,
#   including the "Background" layer group.
# * Within each of the "Background" layer groups, all layers should be SHOWN.
#
# This script will toggle the visibility state of the appropriate "Background" layer
# group, the individual ward layers, and the border.
#
# Close the SVG file before running this script.

# Each svg file should be structured as follows:
# * Layer "Cut 2.5 x 3.5" (with outline of 2.5x3.5 card)
#   * Rect id = "cut-line"
# * Layer "Map border" (black map outline)
#   * Rect id = "map-border-rect"
# * Layer "Size 2.74 x 3.74 MPC" (MPC export layer)
#   * Rect id = "mpc-bbox"
#   * For exporting with bleed
#
# There are 3 groups of ward layers:
# * "B&W" for black and white cards (used for ptint and play)
# * "Clip" for cards with rounded corners (used for docs and pnp)
# * "Bleed" for cards where the image bleeds past the card boundar (for printing)
#
# For each ward group, there is a:
#
#   Set of ward layers, where:
#   * Layer with name given in array (e.g.: "01-chiyoda")
#     * Item with id = layer_name + "_title" (e.g.: "01-chiyoda-title")
#   The "map-border-rect" will automatically be shown for each ward card.
#
#   A group of background layers that contains the water and outlines for the
#   other wards.
#
# For card back (if present):
# * Layer "Card back"
#   * Rect id = "card-back"
#
# Note that the layer names are not required, but the svg ids must be set correctly.

# To export:
# * Cards for use in documentation, export id = "cut-line"
# * Cards for sending to be printed, export id = "mpc-bbox"

import os
import subprocess

from shutil import copyfile

_export_dpi = 300

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
	"haringey",
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
		"--export-dpi=%d" % _export_dpi,
		"--export-text-to-path",
		"--export-id=%s" % id,
		])

# dir: Working directory
# output_dirname: Target dir where exported files will be written
# basename: Name of input SVG
# wards: Array of base filenames
# export_id: The svg id to export for each card
#     Note: Layer ids cannot be exported, so this must be an object in the layer.
# has_back: Does the file include a card back image?
# should_clip: if true, generate clipped cards (rounded corners with transparency)
# should_bw: if true, generate black and white (clipped) cards
def export_png(dir, output_dirname, basename, wards, export_id, has_back, should_clip, should_bw):
	
	src = os.path.join(dir, '%s.svg' % basename)
	background_svg = os.path.join(dir, '%s-background.svg' % basename)
	cutline_svg = os.path.join(dir, '%s-cutline.svg' % basename)
	ku_svg = os.path.join(dir, '%s-out.svg' % basename)

	mod = ''
	if should_clip:
		mod = '-clip'
	if should_bw:
		mod = '-bw'
		
	# Show background layers.
	copyfile(src, background_svg)
	show_layer(background_svg, 'background-map%s' % mod)

	# Create SVG file with card cutline.
	# If we're exporting the full card with bleed, then don't show cutline, just make
	# a copy of the file for the next stage.
	copyfile(background_svg, cutline_svg)
	if export_id == "cut-line":
		show_layer(cutline_svg, 'cut-line')

	outdir = os.path.join(dir, output_dirname)
	if not os.path.isdir(outdir):
		os.makedirs(outdir);

	for layer in wards:
		# Create SVG file with ku map.
		copyfile(cutline_svg, ku_svg)
		show_layer(ku_svg, '%s-title%s' % (layer, mod))

		# Export ku PNG.
		svg_export_id(export_id, ku_svg, os.path.join(outdir, '%s.png' % layer))

	if has_back and not should_bw:
		# Create SVG file for back (no map border).
		copyfile(cutline_svg, ku_svg)
		show_layer(ku_svg, 'card-back')
		svg_export_id(export_id, ku_svg, os.path.join(outdir, 'back.png'))

	os.remove(ku_svg)
	os.remove(cutline_svg)
	os.remove(background_svg)
	

# Tokyo
# Cards for printing with MPC
export_png('.', 'ku-cards', 'ku-cards', _wards, "mpc-bbox", True, False, False)
# Cards clipped to the  cut line
export_png('.', 'ku-cards-clip', 'ku-cards', _wards, "cut-line", True, True, False)
# Cards B&W
export_png('.', 'ku-cards-bw', 'ku-cards', _wards, "cut-line", True, True, True)

# Paris
#export_png('paris', 'arr-cards', 'arr-cards', _arr, "cut-line", False)
#export_png('paris', 'arr-cards', 'arr-cards', _arr, "mpc-bbox", False)

# London
#export_png('london', 'london-cards', 'london-cards', _london, "mpc-bbox", False)
