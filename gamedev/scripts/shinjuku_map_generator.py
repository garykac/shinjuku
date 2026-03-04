#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../../../python-lib')

from ghostscript import GhostScript
from imagemagick import ImageMagick
from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

A4_WIDTH = 2480
A4_HEIGHT = 3508

LETTER_WIDTH = 2550
LETTER_HEIGHT = 3300

TEMP_PNG = "_temp.png"

class ShinjukuMapGenerator:
	def __init__(self, dir, options):
		self.dir = dir
		self.options = options
		
	def export_map(self):
		print("Exporting map...")
		svg = os.path.join(self.dir, self.options['map_svg'])

		map_dir = os.path.join(self.dir, self.options['map_dir'])
		if not os.path.isdir(map_dir):
			os.makedirs(map_dir);

		png = os.path.join(map_dir, f"{self.options['map_basename']}.png")
		jpg = os.path.join(map_dir, f"{self.options['map_basename']}.jpg")
		temp_png = os.path.join(map_dir, TEMP_PNG)
		self.export_map_png(svg, temp_png)
		ImageMagick.force_300_dpi(temp_png, png)
		ImageMagick.png_to_jpg(png, 80, jpg)
		os.remove(temp_png)

	def export_map_png(self, svg, png):
		actions = InkscapeActions()

		actions.exportFilename(png)
		if self.options["map_landscape"]:
			actions.exportSize(6600, 6000)
		else:
			actions.exportSize(6000, 6600)
		actions.exportId(self.options["map_export"])
		actions.exportDo()
		Inkscape.run_actions(svg, actions)
	
	def export_split_pdf(self):
		print("Exporting map into split pdf files...")
		map_dir = os.path.join(self.dir, self.options['map_dir'])
		png = os.path.join(map_dir, f"{self.options['map_basename']}.png")
		padded_png = os.path.join(map_dir, 'map_pad.png')
		rotate = self.options["map_landscape"]

		# Add white border padding so each split tile is the same size.
		print("...padding map image...")
		ImageMagick.expand_for_splitting(png, padded_png, 6300, 9000, rotate)

		# Split padded into into tiles.
		print("...splitting into tiles...")
		tile_png = os.path.join(map_dir, 'tile.png')
		ImageMagick.split_into_tiles(padded_png, tile_png, 3, 3)
		
		print("...creating pdf pages...")
		for i in range(0, 9):
			png = os.path.join(map_dir, f'tile-{i}.png')
			a4_pdf = os.path.join(map_dir, f'tile-{i}-a4.pdf')
			ImageMagick.create_pdf_page(png, a4_pdf, A4_WIDTH, A4_HEIGHT, 45, 60)
			letter_pdf = os.path.join(map_dir, f'tile-{i}-letter.pdf')
			ImageMagick.create_pdf_page(png, letter_pdf, LETTER_WIDTH, LETTER_HEIGHT, 55, 35)

		print("...combining pdfs...")
		pdf_name = f"{self.options['map_basename']}-a4.pdf"
		out_pdf = os.path.join(map_dir, pdf_name)
		in_pdfs = [os.path.join(map_dir, f'tile-{x}-a4.pdf') for x in range(0,9)]
		GhostScript.combine_pdfs(out_pdf, in_pdfs)
				
		pdf_name = f"{self.options['map_basename']}-letter.pdf"
		out_pdf = os.path.join(map_dir, pdf_name)
		in_pdfs = [os.path.join(map_dir, f'tile-{x}-letter.pdf') for x in range(0,9)]
		GhostScript.combine_pdfs(out_pdf, in_pdfs)

		# Cleanup.
		os.remove(padded_png)
		for i in range(0, 9):
			os.remove(os.path.join(map_dir, f'tile-{i}.png'))
			os.remove(os.path.join(map_dir, f'tile-{i}-a4.pdf'))
			os.remove(os.path.join(map_dir, f'tile-{i}-letter.pdf'))
