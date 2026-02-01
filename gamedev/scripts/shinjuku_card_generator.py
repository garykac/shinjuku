#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import os
import platform
import re
import subprocess
import sys

sys.path.append('../../../python-lib')

from ghostscript import GhostScript
from imagemagick import ImageMagick
from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

class ShinjukuCardGenerator:
	def __init__(self, options):
		self.options = options
	
	# Export cards for each ward (standard size and with bleed).
	
	def export_cards(self, dir):
		wards = self.options['wards']
		self.export_wards_png(dir, wards)
		self.export_wards_png_bleed(dir, wards)

	def export_wards_png(self, dir, wards):
		print("Exporting png:")
		outdir = self.options['card_png_dir']
		self.export_ward_cards(dir, 'card-export', 750, 1050, outdir, wards)

	def export_wards_png_bleed(self, dir, wards):
		print("Exporting png-bleed:")
		outdir = self.options['card_png_bleed_dir']
		self.export_ward_cards(dir, 'card-export-bleed', 822, 1122, outdir, wards)

	# dir: Working directory
	# export_id: Id of svg element to export
	# width: width in pixels of output
	# height: height in pixels of output
	# output_dirname: Target dir where exported files will be written
	# wards: Array of ward names
	def export_ward_cards(self, dir, export_id, width, height, output_dirname, wards):
		src_svg = os.path.join(dir, self.options['card_svg'])

		outdir = os.path.join(dir, output_dirname)
		if not os.path.isdir(outdir):
			os.makedirs(outdir);

		temp_png = os.path.join(dir, self.options['temp_png'])

		for w in wards:
			print(f"...{w}")
			# Export the card to have the correct width,height (in 300-dpi pixels) for the
			# card. Since the SVG doesn't have the file properly scaled for the card size
			# (because the map image is shared for the cards and board map) Inkscape will
			# automatically calculate the corresponding dpi based on the WxH, which we'll
			# have to correct afterwards to get a proper 300-dpi file of the right size.
			self.export_card(src_svg, ["card-info-layer", f"card-{w}"], export_id, width, height, temp_png)
		
			# Force dpi to be 300 (without scaling the image).
			ImageMagick.force_300_dpi(temp_png, os.path.join(outdir, f'{w}.png'))

		os.remove(temp_png)

	# Export a single card.
	def export_card(self, svg, layers, export_id, width, height, png):
		actions = InkscapeActions()

		for layer in layers:
			actions.layerShow(layer)

		actions.exportFilename(png)
		#actions.exportDpi(300)
		actions.exportSize(width, height)
		actions.exportId(export_id)
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export card backs (with and without bleed).

	def export_card_backs(self, dir):
		print("Exporting card backs")
		svg = os.path.join(dir, self.options['card_back_svg'])
		card_back_png = self.options['card_back_png']
		self.export_card_back(svg, "export-rect",
				os.path.join(*[dir, self.options['card_png_dir'], card_back_png]))
		self.export_card_back(svg, "export-rect-bleed",
				os.path.join(*[dir, self.options['card_png_bleed_dir'], card_back_png]))

	def export_card_back(self, svg, export_id, png):
		actions = InkscapeActions()
		actions.exportFilename(png)
		actions.exportDpi(300)
		actions.exportId(export_id)
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export 18-up pages for PrintPlayGames.
	
	def export_18up(self, dir):
		src_svg = os.path.join(dir, self.options['ppg_18up_svg'])
	
		outdir = os.path.join(dir, self.options['ppg_18up_dir'])
		if not os.path.isdir(outdir):
			os.makedirs(outdir);
	
		print("Exporting ppg 18-up:")
		for page in ['_back', 'page01', 'page02', 'page03', 'page04']:
			print(f"...{page}")
			out_png = os.path.join(outdir, f'{page}.png')
			self.export_18up_page(src_svg, page, out_png)

	def export_18up_page(self, svg, name, png):
		actions = InkscapeActions()
		actions.exportFilename(png)
		actions.layerShow(f"sheet-{name}")
		actions.exportDpi(300)
		actions.exportAreaPage()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export 9-up pages for print-n-play.
	
	def export_9up(self, dir):
		pdf_basename = self.options['card_out_pdf_basename']
		self.export_9up_type(dir, pdf_basename, "letter")
		self.export_9up_type(dir, pdf_basename, "a4")

	def export_9up_type(self, dir, pdf_basename, type):
		card_dir = self.options['card_dir']
		src_svg = os.path.join(dir, card_dir, f'pnp-9up-{type}.svg')
		out_pdf = os.path.join(dir, card_dir, f'{pdf_basename}-{type}.pdf')

		outdir = os.path.join(dir, card_dir, f'pnp-9up-{type}-pdf')
		if not os.path.isdir(outdir):
			os.makedirs(outdir);
	
		print(f"Exporting pnp 9up ({type}):")
		pages = [f'page{x:02}' for x in range(1,9)]
		for page in ['_back', *pages]:
			print(f"...{page}")
			page_out_pdf = os.path.join(outdir, f'{page}.pdf')
			self.export_9up_page(src_svg, page, page_out_pdf)
		print("Combining 9up pages")
		self.combine_9up(dir, outdir, out_pdf)

	def export_9up_page(self, svg, name, pdf):
		actions = InkscapeActions()
		actions.exportFilename(pdf)
		actions.layerShow(name)
		actions.exportDpi(300)
		actions.exportAreaPage()
		actions.exportTextToPath()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	def combine_9up(self, dir, in_pdf_dir, out_pdf):
		out_pdf = os.path.join(dir, out_pdf)
		in_pdfs = []
		for pdf in [f'page{x:02}.pdf' for x in range(1,9)]:
			in_pdfs.append(os.path.join(dir, in_pdf_dir, pdf))
		GhostScript.combine_pdfs(out_pdf, in_pdfs)

	# Export map.
	
	def export_map(self, dir):
		print("Exporting map...")
		svg = os.path.join(dir, self.options['map_svg'])
		png = os.path.join(dir, self.options['map_png'])
		temp_png = os.path.join(dir, self.options['temp_png'])
		self.export_map_png(svg, temp_png)
		ImageMagick.force_300_dpi(temp_png, png)
		os.remove(temp_png)

	def export_map_png(self, svg, png):
		actions = InkscapeActions()

		for layer in self.options['map_layers']:
			actions.layerShow(layer)

		actions.exportFilename(png)
		if self.options["map_landscape"]:
			actions.exportSize(6600, 6000)
		else:
			actions.exportSize(6000, 6600)
		actions.exportId(self.options["map_export"])
		actions.exportDo()
		Inkscape.run_actions(svg, actions)
