#!/bin/python3
import os
import sys

slides = "slides.html"

target = sys.argv[1]

os.system("pandoc "+target+".md -t revealjs -s -o"+target+".html -V theme=simple --slide-level=2")
#print(sys.argv)

with open(slides, 'r') as f:
  lines = []
  for line in f.readlines():
    line = line.replace("<h1 class=\"title\">", "<h1 class=\"title\" style=\"margin-top:200px\">")
    lines.append(line)

  with open(slides, 'w+') as f:
    f.writelines(lines)

