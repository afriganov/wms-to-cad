# wtc
WMS to CAD

Routine for importing georefed img to CAD software from WMS service. Most of WMS are in EPGS:3857 and this routine output is hardcoded to EPGS:3765, but that can be easily changed to any other desired CRS.

Routine works in a few steps:

When you initialize AutoLisp code from CAD software it prompts user for 2 points (bottom left and top right) and demanded quality, and creates .txt file from it.

Python script is then initialized from CAD which takes those inputs, transforms input coordinates to desired CRS(in this case 3857) and requests image from WMS.

Image comes back in 3857, then gets transformed to 3765 using gdal. Python code also outputs world file to go with the transformed raster which is then loaded into CAD in the last part of the lisp.


