#!/bin/bash
# This script must be run from the spell-cards/9up directory.

INKSCAPE="/Applications/Inkscape.app/Contents/MacOS/inkscape"

FILES=9
CITY="osaka"

for i in $(seq -f "%02g" 1 $FILES)
do
	echo Generating $CITY map PDF page$i 
	$INKSCAPE --export-filename pdf/page$i.pdf --export-dpi=300 --export-text-to-path --export-area-page svg/page$i.svg
done

# Generate combined PDF.
echo Combining PDFs
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$CITY-map.pdf $(seq -f "pdf/page%02g.pdf" 1 $FILES)
