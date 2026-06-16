#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt
import os
import sys

from shinjuku_card_generator import ShinjukuCardGenerator
from shinjuku_map_generator import ShinjukuMapGenerator

class ShinjukuGenerator():
	def __init__(self, dir, options):
		self.dir = dir
		self.options = options

	def usage(self):
		print(f"Usage: {sys.argv[0]} <options>")
		print("where <options> are:")
		print("  --help [-?]")
		print("  --cards")
		print("  --map")
		print("  --png")
		print("  --ppg")
		exit()

	def Generate(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:],
				'?cm',
				['help', 'cards', 'map', "pnp", "ppg"])
		except getopt.GetoptError:
			self.usage()

		# Primary options.
		gen_cards = False
		gen_map = False

		# Generate 18-up cards for PPG.
		gen_ppg = False
		# Generate 9-up cards and map for PnP.
		gen_pnp = False
	
		for opt, arg in opts:
			if opt in ('-?', '--help'):
				self.usage()
			if opt in ('-c', '--cards'):
				gen_cards = True
			if opt in ('-m', '--map'):
				gen_map = True
			if opt in ('--pnp'):
				gen_pnp = True
			if opt in ('--ppg'):
				gen_ppg = True

		# If no primary options are specified, generate everything.
		if not gen_cards and not gen_map:
			gen_cards = True
			gen_map = True
			gen_pnp = True
			gen_ppg = True

		if gen_cards:
			cardgen = ShinjukuCardGenerator(self.dir, self.options)
			cardgen.export_cards()
			cardgen.export_card_backs()
			if gen_pnp:
				cardgen.export_9up()
			if gen_ppg:
				cardgen.export_18up()

		if gen_map:
			mapgen = ShinjukuMapGenerator(self.dir, self.options)
			mapgen.export_map()
			if gen_pnp:
				mapgen.export_split_pdf()
