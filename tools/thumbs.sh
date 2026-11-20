#!/bin/bash
# Build the round-portrait thumbnails: a 240 px square cut from the top of each still, scaled with a
# smoothing filter and slightly darkened so the thin pencil lines stay solid at 76 to 96 px.
# Run from the repo root: tools/thumbs.sh
mkdir -p figuren/thumb
for f in figuren/*.jpg; do
  magick "$f" -colorspace RGB -filter Lanczos -resize 240x240^ -colorspace sRGB -gravity north -extent 240x240 -gamma 0.72 -unsharp 0x0.6+0.6+0 -quality 90 "figuren/thumb/$(basename "$f")"
done
