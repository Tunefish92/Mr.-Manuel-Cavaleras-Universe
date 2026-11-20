#!/bin/bash
# Build one contact sheet (20 evenly spaced, time-stamped frames) for a video file.
vid="$1"; out="$2"
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$vid")
ffmpeg -v error -y -i "$vid" -vf "fps=20/${dur},scale=384:-2,drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=22:fontcolor=white:box=1:boxcolor=black@0.7,tile=5x4" -frames:v 1 -q:v 4 "$out"
