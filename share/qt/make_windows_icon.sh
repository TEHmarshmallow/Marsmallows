#!/bin/bash
# create multiresolution windows icon
ICON_SRC=../../src/qt/res/icons/Marsmello.png
ICON_DST=../../src/qt/res/icons/Marsmello.ico
convert ${ICON_SRC} -resize 16x16 Marsmello-16.png
convert ${ICON_SRC} -resize 32x32 Marsmello-32.png
convert ${ICON_SRC} -resize 48x48 Marsmello-48.png
convert Marsmello-16.png Marsmello-32.png Marsmello-48.png ${ICON_DST}

