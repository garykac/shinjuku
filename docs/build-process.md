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

Double Check:

* If text has been moved, make sure that it avoids the cuts for a quad-fold board. Show the "Folding Boards" layer to see where they are.

### Export full size images

Export the following map images at 300dpi:

* With Border
   * Layer "Border 18x24" export @300dpi as `tokyo-map-border-300dpi.png` (7200x5400 pixels)
* [optional] Borderless
   * Layer "Border 18x24" export @300dpi as `tokyo-map-300dpi.png` (7200x5400 pixels).
   * Hide Layer "Border 18x24" after selecting rect
   * Used only if sending to be printed (PrintPlayGames).

### Generate compact images

In Affinity Photo, open `map/tokyo-map-border-300dpi.png`:

* Export full size as JPG quality 80 `map/tokyo-map-border-300dpi.jpg`.
	This reduces file size from 22M -> 7M.
* Export 1200x900 as PNG `map/tokyo-map.png`
* Export 1200x900 as JPG quality 80 `map/tokyo-map-sm.jpg`

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

In Inkscape, open `map/tokyo-map.svg`:

* Layer "Border 18x24" export at 150dpi (3600x2700) -> `tmp`

In Affinity Photo, open `tmp`:

* Export 3600x2700 quality 60 as JPG `pnp/shinjuku-pnp/map-color.jpg`

In Inkscape, open `map/tokyo-map.svg` and export the 6 map PNGs that comprise the map

* Show the "7x10 Pages" and "White Outer Border" layers
* Select upper-left rect and then Hide the "7x10 Pages" layer
* Export Selection @ 150dpi into `pnp/map-color/map-1.png` (1050x1500px)
* Repeat for other 7 rects

Convert the 8 PNGs into JPGs with quality 70

Create Color PDF (Letter)

* Open all 8 JPGs in Preview
* Print - set paper to "Letter"
* "Save as PDF"
* Set PDF title "Shinjuku PNP Color Map"
* Save PDF as `pnp/shinjuku-pnp/map-color-letter.pdf`

Create Color PDF (A4)

* Open all 8 JPGs in Preview
* Print - set paper to "A4"
* "Save as PDF"
* Set PDF title "Shinjuku PNP Color Map"
* Save PDF as `pnp/shinjuku-pnp/map-color-a4.pdf`

### Extra Things to Consider

* Do the cards need to be updated with the map changes?

## Rulebook Updates

If the rulebook has been updated:

* Update both the Rules and the Quickstart so that they remain consistent.
* The rules summary on the player screen may need to be updated.
* The rules summary in the github [README.md](../README.md) may need to be updated as well.

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

Duplicate the A4 version, remove `_a4` and add `_vXrY` where X is the current version and Y is the revision.

Upload the updated documents to BoardGameGeek:

* [Shinjuku Rules at BGG](https://boardgamegeek.com/filepage/186374/shinjuku-rules-play)
* [Shinjuku Quickstart at BGG](https://boardgamegeek.com/filepage/186375/shinjuku-quickstart-guide)

## Card Updates

* Make sure all top-level layers are hidden except "B&W", "Clip" and "Bleed" groups.
* Within each of these groups:
	* All layers should be hidden
	* Within the "Background - xxx" group, all layers should be visible (but the "Background" layer is hidden)
* Close Inkscape
* Run the `ku-card-export.py` script from the `cards` directory:
	* Edit the options in the script as needed
	* `python ku-card-export.py`
* Output is written to `cards/ku-cards`, `cards/ku-cards-clip` and `cards/ku-cards-bw`

### Print and Play

* Run `pnp/card-export.py`
	* This will create PNGs in `pnp/cards-color` and `pnp/cards-bw`
* Convert PNGs to JPGs @ 70%
* Select each JPG in order and open in Preview
* Export PDF
	* When exporting, set Title to "Shinjuku PNP Cards"
	* Print/Save as pdf Letter to `pnp/shinjuku-pnp/cards-color.pdf`
	* Print/Save as pdf A4 to `pnp/shinjuku-pnp/cards-color-a4.pdf`
	* Repeat above steps for `-bw` versions

## Player Screen Updates

Export for printing:

* Export page (3600x5400) as `screen/screen-instr.png`

### Tabletop Simulator

Export instructions reference:

* Select "Border - TTS Player Screen Instr" layer
* Select the rectangle
* Hide "Border - TTS Player Screen Instr"
* Export selection @300dpi (2989 x 1405px) as `screen/reference.png`
* Copy to `tts/ref/` directory

### Print and Play

Print out each individual screen (front and back).

For front (with logo):

* Select the "Bleed" ouline (unlock layer first)
* Hide the "Bleed" layer
* Export PNG @ 150dpi.
* Re-lock "Bleed" layer
* Rotate 90deg CW

For backs (with player aid info)

* Show the "Cut/Fold" layer
* Select the "Bleed" ouline (unlock layer first)
* Hide the "Bleed" layer
* Export PNG @ 150dpi
* Re-lock "Bleed" layer
* Rotate 90deg CCW

Export each as 719 x 1541 image:
  front: quality 80 jpg
  back: png

Combine into a PDF by printing from MacOS Preview app (title: "Shinjuku Player Screens"), alternating front/back so that it can be printed double-sided.

Temp screen images are stored in `pnp/screen-pages`. Final files are placed in `pnp/shinjuku-pnp/screens.pdf` (`screens-a4.pdf` for A4 version).

## Variants Updates

### Rulebook

Similar to the main Rulebook/Quickstart Updates:

* Export `docs/shinjuku_variants.afpub` as PDF for Letter and A4

## Print and Play Instruction Updates

PnP instructions no longer include variants.

### Update BGG

If this is a significant update, then update the rules uploaded to BoardGameGeek.

As with the rulebooks, duplicate the A4 version, remove `_a4` and add `_rXX` where XX is the current revision.

Upload the updated documents to BoardGameGeek:

* [Shinjuku Print and Play Instructions at BGG](https://boardgamegeek.com/filepage/187225/shinjuku-print-and-play-instructions)

## Sellsheet

In Inkscape, export the PDF from `docs/shinjuku_sellsheet.svg`.

Upload to ...
