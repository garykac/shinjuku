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

	def Generate(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:],
				'cm',
				['cards', 'map'])
		except getopt.GetoptError:
			usage()

		gen_cards = False
		gen_map = False
	
		for opt, arg in opts:
			if opt in ('-c', '--cards'):
				gen_cards = True
			if opt in ('-m', '--map'):
				gen_map = True
	
		# By default, generate everything.
		if not gen_cards and not gen_map:
			gen_cards = True
			gen_map = True

		if gen_cards:
			cardgen = ShinjukuCardGenerator(self.dir, self.options)
			cardgen.export_cards()
			cardgen.export_card_backs()
			cardgen.export_18up()
			#cardgen.export_9up()

		if gen_map:
			mapgen = ShinjukuMapGenerator(self.dir, self.options)
			mapgen.export_map()
			mapgen.export_split_pdf()
