import os

slides = "slides.html"

with open(slides, 'r') as f:
  lines = []
  for line in f.readlines():
    line = line.replace("<h1 class=\"title\">", "<h1 class=\"title\" style=\"margin-top:200px\">")
    lines.append(line)

  with open(slides, 'w+') as f:
    f.writelines(lines)
