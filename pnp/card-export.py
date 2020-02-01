#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto-generate print-and-play card images from cards.svg.
#
# Before running this script, make sure the SVG file has layers hidden as follows:
#
# * All "Page" layers should be HIDDEN
# * The "Background" layer should be SHOWN
#
# This script will toggle the visibility state of the appropriate "Page" layer
# group, the individual ward layers, and the border.
#
# Close the SVG file before running this script.
#
# Note that the layer names are not required, but the svg ids must be set correctly.

import os
import subprocess

from shutil import copyfile

_export_dpi = 150

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

# basename: Base name of SVG file with card data
def export_png(basename):
	src_svg = '%s.svg' % basename
	tmp_svg = 'card-tmp.svg'

	if not os.path.isdir(basename):
		os.makedirs(basename);

	for page in [1,2,3,4,5,6,7,8]:
		copyfile(src_svg, tmp_svg)
		show_layer(tmp_svg, 'page-%d' % page)

		# Export ku PNG.
		svg_export_id('export', tmp_svg, os.path.join(basename, 'pnp-%s-%d.png' % (basename, page)))

	os.remove(tmp_svg)
	

#export_png('cards-color')
export_png('cards-bw')
