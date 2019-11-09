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
* Layer "View 18x80" export as `tokyo-map-18x20-300dpi.png` (6000x5400 pixels)
  Hide layer after selecting rect
* Layer "View 18x20 + 1/8 bleed" as `tokyo-map-18x20-bleed-300dpi.png`  (6075x5475 pixels)
  Hide layer after selecting rect

### Generate compact images

In Affinity Photo, open `map/tokyo-map-border-300dpi.png`:

* Export full size as JPG quality 80 `map/tokyo-map-border-300dpi.jpg`
	This reduces file size from 22M -> 7M
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

### Extra Things to Check

* Do the cards need to be updated with the map changes?
* Do the Print and Play files need to be updated?

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

If this is a significant update, then update the rules on BoardGameGeek.

Duplicate the A4 version, remove `_a4` and add `_rXX` where XX is the current revision.

Upload the updated documents to BoardGameGeek:

* [Shinjuku Rules at BGG](https://boardgamegeek.com/filepage/186374/shinjuku-rules-play)
* [Shinjuku Quickstart at BGG](https://boardgamegeek.com/filepage/186375/shinjuku-quickstart-guide)

## Player Screen Updates

TODO

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
