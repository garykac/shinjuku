#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys

sys.path.append('../../../python-lib')

from ghostscript import GhostScript
from imagemagick import ImageMagick
from inkscape import Inkscape, InkscapeActions
from shutil import copyfile

TEMPLATE_DIR = "templates"

TEMP_DIR = "_combined"
TEMP_PNG = "_temp.png"

class ShinjukuCardGenerator:
	def __init__(self, dir, options):
		self.dir = dir
		self.options = options
		
		self.card_dir = os.path.join(dir, options['card_dir'])
		self.template_dir = os.path.join(os.path.dirname(__file__), TEMPLATE_DIR)

		# Build array of cards with each one duplicated the appropriate number of times.	
		# Validate card counts.
		self.deck = []
		counts = options['ward_counts']
		for w in counts:
			self.deck.extend([w] * counts[w])
		if len(self.deck) != 72:
			print(f"Invalid card count {len(self.deck)} != 72")
			sys.exit()
	
	# Export cards for each ward (standard size and with bleed).
	
	def export_cards(self):
		wards = self.options['wards']
		self.export_wards_png(wards)
		self.export_wards_png_bleed(wards)

	def export_wards_png(self, wards):
		print("Exporting png:")
		outdir = os.path.join(self.card_dir, self.options['card_png_dir'])
		self.export_ward_cards('card-export', 750, 1050, outdir, wards)

	def export_wards_png_bleed(self, wards):
		print("Exporting png-bleed:")
		outdir = os.path.join(self.card_dir, self.options['card_png_bleed_dir'])
		self.export_ward_cards('card-export-bleed', 822, 1122, outdir, wards)

	# export_id: Id of svg element to export
	# width: width in pixels of output
	# height: height in pixels of output
	# output_dirname: Target dir where exported files will be written
	# wards: Array of ward names
	def export_ward_cards(self, export_id, width, height, output_dirname, wards):
		src_svg = os.path.join(self.dir, self.options['card_svg'])

		outdir = os.path.join(self.dir, output_dirname)
		if not os.path.isdir(outdir):
			os.makedirs(outdir);

		card_layers = self.options['card_layers']
		for w in wards:
			print(f"...{w}")

			# List of layers to make visible.
			layers = [f"card-{w}"]
			layers += self.options['card_layers_common'].copy()
			if w in card_layers:
				layers += card_layers[w]
			
			outpng = os.path.join(outdir, f'{w}.png')
			self.export_card(src_svg, layers, export_id, width, height, outpng)

	# Export a single card from an SVG with the specified layers made visible.
	def export_card(self, svg, layers, export_id, width, height, png):
		temp_png = os.path.join(self.card_dir, TEMP_PNG)

		# Export the card to have the correct width,height (in 300-dpi pixels) for the
		# card. Since the SVG doesn't have the file properly scaled for the card size
		# (because the map image is shared for the cards and board map) Inkscape will
		# automatically calculate the corresponding dpi based on the WxH, which we'll
		# have to correct afterwards to get a proper 300-dpi file of the right size.
		actions = InkscapeActions()

		for layer in layers:
			actions.layerShow(layer)

		actions.exportFilename(temp_png)
		#actions.exportDpi(300)
		actions.exportSize(width, height)
		actions.exportId(export_id)
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

		# Force dpi to be 300 (without scaling the image).
		ImageMagick.force_300_dpi(temp_png, png)

		os.remove(temp_png)

	# Export card backs (with and without bleed).

	def export_card_backs(self):
		print("Exporting card backs")
		svg = os.path.join(self.card_dir, self.options['card_back_svg'])
		card_back_png = self.options['card_back_png']
		self.export_card_back(svg, "export-rect",
				os.path.join(*[self.card_dir, self.options['card_png_dir'], card_back_png]))
		self.export_card_back(svg, "export-rect-bleed",
				os.path.join(*[self.card_dir, self.options['card_png_bleed_dir'], card_back_png]))

	def export_card_back(self, svg, export_id, png):
		actions = InkscapeActions()
		actions.exportFilename(png)
		actions.exportDpi(300)
		actions.exportId(export_id)
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export 18-up pages for PrintPlayGames.
	
	def export_18up(self):
		print("Exporting ppg 18-up:")
		self.export_18up_back()
		self.export_18up_pages()

	def export_18up_back(self):
		# Copy the ppg-18-up template.
		src_template = os.path.join(self.template_dir, "ppg-18up-flipped.svg")
		template = os.path.join(self.card_dir, "_template.svg")
		shutil.copy(src_template, template)

		outdir = os.path.join(self.card_dir, self.options['ppg_18up_dir'])
		if not os.path.isdir(outdir):
			os.makedirs(outdir);

		bleed_dir = os.path.join(self.card_dir, self.options['card_png_bleed_dir'])
		print(f"...back")
		for x in range(0, 18):
			src = os.path.join(bleed_dir, "_back.png")
			dst = os.path.join(self.card_dir, f"_card-{x:02}.png")
			shutil.copy(src, dst)

		out_png = os.path.join(outdir, 'page-back.png')
		self.export_page(template, [], out_png)

		self.cleanup_18up_files(template)

	def export_18up_pages(self):
		# Copy the ppg-18-up template.
		src_template = os.path.join(self.template_dir, "ppg-18up.svg")
		template = os.path.join(self.card_dir, "_template.svg")
		shutil.copy(src_template, template)
		
		outdir = os.path.join(self.card_dir, self.options['ppg_18up_dir'])
		if not os.path.isdir(outdir):
			os.makedirs(outdir);

		ppg18_deck = self.deck.copy()
		
		# Copy batch of card images for template.
		bleed_dir = os.path.join(self.card_dir, self.options['card_png_bleed_dir'])
		for page in range(1, 5):
			print(f"...page {page}")
			for x in range(0, 18):
				ward = ppg18_deck.pop(0)
				src = os.path.join(bleed_dir, f"{ward}.png")
				dst = os.path.join(self.card_dir, f"_card-{x:02}.png")
				shutil.copy(src, dst)

			out_png = os.path.join(outdir, f'page-{page:02}.png')
			self.export_page(template, [], out_png)

		self.cleanup_18up_files(template)

	def cleanup_18up_files(self, template):
		os.remove(template)
		for x in range(0, 18):
			temp = os.path.join(self.card_dir, f"_card-{x:02}.png")
			os.remove(temp)
			
	def export_page(self, svg, layers, png):
		actions = InkscapeActions()
		actions.exportFilename(png)
		for layer in layers:
			actions.layerShow(layer)
		actions.exportDpi(300)
		actions.exportAreaPage()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export 9-up pages for print-n-play.
	
	def export_9up(self):
		pdf_basename = self.options['card_out_pdf_basename']
		self.export_9up_type(pdf_basename, "letter")
		self.export_9up_type(pdf_basename, "a4")

	def export_9up_type(self, pdf_basename, type):
		card_dir = self.options['card_dir']
		src_svg = os.path.join(self.dir, card_dir, f'pnp-9up-{type}.svg')
		out_pdf = os.path.join(self.dir, card_dir, f'{pdf_basename}-{type}.pdf')

		outdir = os.path.join(self.dir, card_dir, f'pnp-9up-{type}-pdf')
		if not os.path.isdir(outdir):
			os.makedirs(outdir);
	
		print(f"Exporting pnp 9up ({type}):")
		pages = [f'page{x:02}' for x in range(1,9)]
		for page in ['_back', *pages]:
			print(f"...{page}")
			page_out_pdf = os.path.join(outdir, f'{page}.pdf')
			self.export_9up_page(src_svg, page, page_out_pdf)
		print("Combining 9up pages")
		self.combine_9up(outdir, out_pdf)

	def export_9up_page(self, svg, name, pdf):
		actions = InkscapeActions()
		actions.exportFilename(pdf)
		actions.layerShow(name)
		actions.exportDpi(300)
		actions.exportAreaPage()
		actions.exportTextToPath()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	def combine_9up(self, in_pdf_dir, out_pdf):
		out_pdf = os.path.join(self.dir, out_pdf)
		in_pdfs = []
		for pdf in [f'page{x:02}.pdf' for x in range(1,9)]:
			in_pdfs.append(os.path.join(self.dir, in_pdf_dir, pdf))
		GhostScript.combine_pdfs(out_pdf, in_pdfs)
