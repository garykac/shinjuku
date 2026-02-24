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

PPG_18UP_DIR = 'ppg-18up'

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

	def make_card_subdir(self, dirname):
		subdir = os.path.join(self.card_dir, dirname)
		if not os.path.isdir(subdir):
			os.makedirs(subdir)
		return subdir

	def copy_template(self, template, dir, temp_template):
		src_template = os.path.join(self.template_dir, template)
		t = os.path.join(dir, temp_template)
		shutil.copy(src_template, t)
		return t

	# Export svg page to png.
	# Entire page is exported unless |export_id| is specified.
	def export_page_png(self, svg, layers, png, export_id = None):
		actions = InkscapeActions()
		actions.exportFilename(png)
		for layer in layers:
			actions.layerShow(layer)
		actions.exportDpi(300)
		if export_id:
			actions.exportId(export_id)
		else:
			actions.exportAreaPage()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	def export_page_pdf(self, svg, layers, pdf):
		actions = InkscapeActions()
		actions.exportFilename(pdf)
		for layer in layers:
			actions.layerShow(layer)
		actions.exportDpi(300)
		actions.exportAreaPage()
		actions.exportTextToPath()
		actions.exportDo()
		Inkscape.run_actions(svg, actions)

	# Export cards for each ward (standard size and with bleed).
	
	def export_cards(self):
		wards = self.options['wards']
		self.export_wards_png(wards)
		self.export_wards_png_bleed(wards)

	def export_wards_png(self, wards):
		print("Exporting png:")
		self.export_ward_cards('card-export', 750, 1050, self.options['card_png_dir'], wards)

	def export_wards_png_bleed(self, wards):
		print("Exporting png-bleed:")
		self.export_ward_cards('card-export-bleed', 822, 1122, self.options['card_png_bleed_dir'], wards)

	# export_id: Id of svg element to export
	# width: width in pixels of output
	# height: height in pixels of output
	# output_dirname: Target dir where exported files will be written
	# wards: Array of ward names
	def export_ward_cards(self, export_id, width, height, output_dirname, wards):
		src_svg = os.path.join(self.dir, self.options['card_svg'])

		outdir = self.make_card_subdir(output_dirname)

		for w in wards:
			print(f"...{w}")

			# List of layers to make visible.
			layers = []
			
			if 'card_layers_common' in self.options:
				layers.extend(self.options['card_layers_common'].copy())

			if 'auto_card_layers' in self.options:
				layer_prefixes = self.options['auto_card_layers']
				for layer_prefix in layer_prefixes:
					layers.append(f"{layer_prefix}{w}")
				
			if 'auto_card_layer_count' in self.options:
				layer_prefix = self.options['auto_card_layer_count']
				card_count = self.options['ward_counts'][w]
				layers.append(f"{layer_prefix}{card_count}")
				
			if 'auto_card_layer_color' in self.options:
				layer_prefix = self.options['auto_card_layer_color']
				card_color = self.options['ward_colors'][w]
				layers.append(f"{layer_prefix}{card_color}")
			
			if w in self.options['wards_with_dept_store']:
				layers.append("dept-store-hex-index")
				
			outpng = os.path.join(outdir, f'{w}.png')
			self.export_card(src_svg, layers, export_id, width, height, outpng)

	# Export a single card from an SVG with the specified layers made visible.
	def export_card(self, svg, layers, export_id, width, height, png):
		temp_png = os.path.join(self.card_dir, TEMP_PNG)

		# Export the card to have the correct width,height (in 300-dpi pixels) for the
		# card. Since the SVG may not have the file properly scaled for the card size
		# (because the map image can be shared for the cards and board map) Inkscape will
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
		self.export_page_png(svg, [],
				os.path.join(*[self.card_dir, self.options['card_png_dir'], card_back_png]),
				"export-rect")
		self.export_page_png(svg, [],
				os.path.join(*[self.card_dir, self.options['card_png_bleed_dir'], card_back_png]),
				"export-rect-bleed")

	# Export 18-up pages for PrintPlayGames.
	
	def export_18up(self):
		print("Exporting ppg 18-up:")
		self.export_18up_back()
		self.export_18up_pages()

	def export_18up_back(self):
		template = self.copy_template("ppg-18up-flipped.svg", self.card_dir, "_template.svg")

		outdir = self.make_card_subdir(PPG_18UP_DIR)
		bleed_dir = self.make_card_subdir(self.options['card_png_bleed_dir'])

		print(f"...back")
		for x in range(0, 18):
			src = os.path.join(bleed_dir, "_back.png")
			dst = os.path.join(self.card_dir, f"_card-{x:02}.png")
			shutil.copy(src, dst)

		out_png = os.path.join(outdir, 'page-back.png')
		self.export_page_png(template, [], out_png)

		self.cleanup_18up_files(template)

	def export_18up_pages(self):
		template = self.copy_template("ppg-18up.svg", self.card_dir, "_template.svg")
		
		outdir = self.make_card_subdir(PPG_18UP_DIR)
		bleed_dir = os.path.join(self.card_dir, self.options['card_png_bleed_dir'])
		
		# Copy batch of card images for template.
		ppg18_deck = self.deck.copy()
		for page in range(1, 5):
			print(f"...page {page}")
			for x in range(0, 18):
				ward = ppg18_deck.pop(0)
				src = os.path.join(bleed_dir, f"{ward}.png")
				dst = os.path.join(self.card_dir, f"_card-{x:02}.png")
				shutil.copy(src, dst)

			out_png = os.path.join(outdir, f'page-{page:02}.png')
			self.export_page_png(template, [], out_png)

		self.cleanup_18up_files(template)

	def cleanup_18up_files(self, template):
		os.remove(template)
		for x in range(0, 18):
			temp = os.path.join(self.card_dir, f"_card-{x:02}.png")
			os.remove(temp)
			
	# Export 9-up pages for print-n-play.
	
	def export_9up(self):
		print("Exporting pnp 9up:")
		pdf_basename = self.options['card_out_pdf_basename']
		xdir = self.make_card_subdir("_pnp9up")
		outdir = self.make_card_subdir("pnp-9up")
		t_letter = self.copy_template("pnp-9up-letter.svg", xdir, "_template_letter.svg")
		t_a4 = self.copy_template("pnp-9up-a4.svg", xdir, "_template_a4.svg")
		png_dir = os.path.join(self.card_dir, self.options['card_png_dir'])

		# Copy card back images for templates.
		print(f"...back")
		for x in range(0, 9):
			src = os.path.join(png_dir, f"_back.png")
			dst = os.path.join(xdir, f"_card-{x:02}.png")
			shutil.copy(src, dst)
		out_pdf = os.path.join(outdir, f'{pdf_basename}-a4-back.pdf')
		self.export_page_pdf(t_a4, [], out_pdf)
		out_pdf = os.path.join(outdir, f'{pdf_basename}-letter-back.pdf')
		self.export_page_pdf(t_letter, [], out_pdf)
		
		# Copy batch of card images for templates.
		pnp9_deck = self.deck.copy()
		for page in range(1, 9):
			print(f"...page {page}")
			for x in range(0, 9):
				ward = pnp9_deck.pop(0)
				src = os.path.join(png_dir, f"{ward}.png")
				dst = os.path.join(xdir, f"_card-{x:02}.png")
				shutil.copy(src, dst)

			out_pdf = os.path.join(xdir, f'a4-page-{page:02}.pdf')
			self.export_page_pdf(t_a4, [], out_pdf)

			out_pdf = os.path.join(xdir, f'letter-page-{page:02}.pdf')
			self.export_page_pdf(t_letter, [], out_pdf)

		print("Combining 9up pages")
		for type in [ "a4", "letter" ]:
			out_pdf = os.path.join(outdir, f'{pdf_basename}-{type}.pdf')
			in_pdfs = []
			for pdf in [f'{type}-page-{x:02}.pdf' for x in range(1,9)]:
				in_pdfs.append(os.path.join(xdir, pdf))
			GhostScript.combine_pdfs(out_pdf, in_pdfs)

		shutil.rmtree(xdir)
