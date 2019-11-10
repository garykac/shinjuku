# Shinjuku Build Process

Documentation to ensure that the build/release process is performed consistently when updates are made to the documentation.

Many of these steps are manual because they are done infrequently.
Tasks that happen more often will typically be streamlined using scripts.

## General Rule Updates

When updating/clarifying the rules, there are 5 places that may need to be updated:

* Main rules of play doc (`docs/shinjuku_rules.afpub`)
* Quickstart doc (`docs/shinjuku_quickstart.afpub`)
* Player screen (`screen/screen.svg`)
* Rule summary on Github (`README.md`)
* Sellsheet (`docs/shinjuku_sellsheet.svg`)
	
## Map Updates

If the map (`map/tokyo-map.svg`) has been updated:

### Export full size images

Export the following map images at 300dpi:

* Layer "Border 18x20" export as `tokyo-map-border-300dpi.png` (6000x5400 pixels)
* Layer "View 18x20 + 1/8 bleed" as `tokyo-map-bleed-300dpi.png`  (6075x5475 pixels).
  Hide layer after selecting rect.
  Used only for sending to be printed.

### Generate compact images

In Affinity Photo, open `map/tokyo-map-border-300dpi.png`:

* Export full size as JPG quality 80 `map/tokyo-map-border-300dpi.jpg`.
	This reduces file size from 22M -> 7M.
* Export 1000x900 as PNG `map/tokyo-map.png`
* Export 1000x900 as JPG quality 80 `map/tokyo-map-sm.jpg`

### Update map archive

Update `archive/tokyo-map` images with the 1000x900px png and jpg files.

### Update rulebook images

Each map image in the rulebook has a corresponding "Overlay" layer in the map SVG file.

To export an overlay image

* Show the "Overlay Background" layer. This lightens the map so that the pieces stand out.
* Show the layer to be exported (e.g., "Overlay: Move Example 1")
* Select the bounding box in this layer
* Temporarily hide the bounding box by turning off the stroke
* Export the selection at 150dpi. Because the name is associated with the bounding box, it will default to the correct value.
* Re-enable the bounding box stroke
* Re-hide the layer and the Overlay Background layer.

### Generate color maps for PNP

In Affinity Photo, open `map/tokyo-map-border-300dpi.png`:

* Export 3000x2700 quality 60 as JPG `pnp/shinjuku-pnp/map-color.png`

In Inkscape, open `map/tokyo-map.svg` and export the 6 map PNGs that comprise the map

* Show the "7x10 Pages" and "White Outer Border" layers
* Select upper-left rect and then Hide the "7x10 Pages" layer
* Export Selection @ 150dpi into `pnp/map-color/map-1.png` (1050x1500px)
* Repeat for other 5 rects

Convert the 6 PNGs into JPGs with quality 70

Create Color PDF (Letter)

* Open all 6 JPGs in Preview
* Print - set paper to "Letter"
* "Save as PDF"
* Set PDF title "Shinjuku PNP Color Map"
* Save PDF as `pnp/shinjuku-pnp/map-color-letter.pdf`

Create Color PDF (A4)

* Open all 6 JPGs in Preview
* Print - set paper to "A4"
* "Save as PDF"
* Set PDF title "Shinjuku PNP Color Map"
* Save PDF as `pnp/shinjuku-pnp/map-color-a4.pdf`

### Generate B&W maps for PNP

Process is basically the same as color pnp maps except save files in `map-bw` instead of `map-color`.

Hide the following layers:

* "Station Shadows"
* "Wards - Color"
* "Water Boundaries Clone - Shadow"

And show:

* "Ku Names - B&W"
* "Wards - Black Outline"
* "Wards - B&W"
* "Water Boundaries Clone - Dot B&W"
* "Water - B&W"

In Inkscape, export the following map images at 300dpi:

* Layer "Border 18x20" export as `tokyo-map-bw-300dpi.png` (6000x5400 pixels)

In Affinity Photo, open `map/tokyo-map-bw-300dpi.png`:

* Export 3000x2700 quality 60 as JPG `pnp/shinjuku-pnp/map-bw.png`

In Inkscape, export the 6 7x10" maps images as for color maps. Save images as `pnp/map-bw/` directory.

Create PDFs as for color maps. Final PDFs should be stored in `pnp/shinjuku-pnp/map-bw-letter.pdf` and `pnp/shinjuku-pnp/map-bw-a4.pdf`

### Extra Things to Check

* Do the cards need to be updated with the map changes?

## Rulebook Updates

If the rulebook has been updated:

* Update both the Rules and the Quickstart so that they remain consistent.
* The rules summary on the player screen may need to be updated.
* The rules summary in the github [README.md](../README.md) need to be updated as well.

### Export both Letter and A4

In Affinity Publisher, open `docs/shinjuku_rules.afpub`:

* Export A4
  * Open "Spread Setup", select "All Spreads" and set to "A4"
  * Export PDF into `docs/shinjuku_rules_a4.pdf`

* Export Letter
  * Open "Spread Setup", select "All Spreads" and set to "Letter (ANSI A)"
  * Export PDF into `docs/shinjuku_rules.pdf`

Repeat for `docs/shinjuku_quickstart.afpub`

### Update BGG

If this is a significant update, then update the rules uploaded to BoardGameGeek.

Duplicate the A4 version, remove `_a4` and add `_rXX` where XX is the current revision.

Upload the updated documents to BoardGameGeek:

* [Shinjuku Rules at BGG](https://boardgamegeek.com/filepage/186374/shinjuku-rules-play)
* [Shinjuku Quickstart at BGG](https://boardgamegeek.com/filepage/186375/shinjuku-quickstart-guide)

## Card Updates

* Make sure all layers are hidden except "Background outlines" and "Water"
* Close Inkscape
* Run the `ku-card-export.py` script from the `cards` directory:
  * Edit the options in the script
  * `python ku-card-export.py`
* Output is written to `cards/ku-cards`, copy to new location if necessary

## Player Screen Updates

Print out each individual screen (front and back) and combine into a PDF. Flip the images so that they can be printed double-sided.

## Expansion Pack Updates

### Rulebook

Similar to the main Rulebook/Quickstart Updates:

* Export `docs/shinjuku_ex_1.afpub` as PDF for Letter and A4

## Print and Play Updates

To update the PNP instructions, there are 2 places that need to be kept in sync:

* The downloadable PDF
* The online markdown file: [pnp/index.md](../pnp/index.md)

Similar to the main Rulebook/Quickstart Updates:

* Export `pnp/shinjuku_pnp_instr.afpub` as PDF for Letter/A4

Except that the PDF files should be saved in `pnp/shinjuku-pnp` directory.

## Sellsheet

In Inkscape, export the PDF from `docs/shinjuku_sellsheet.svg`.

Upload to ...
