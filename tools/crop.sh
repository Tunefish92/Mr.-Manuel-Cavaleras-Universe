#!/bin/bash
# Cut one still per character, using the very frame the contact sheet showed (same fps filter, tile index from the time stamp).
while IFS=$'\t' read -r name vid t box; do
  set -- $box
  f=$(ls vid/"$vid".* | head -1)
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  k=$(python3 -c "print(round($t*20/$dur))")
  ffmpeg -v error -y -i "$f" -vf "fps=20/${dur},select=eq(n\,$k),crop=iw*($3-$1):ih*($4-$2):iw*$1:ih*$2" -frames:v 1 -q:v 2 "out/figuren/$name.jpg" </dev/null
done < crops.tsv
