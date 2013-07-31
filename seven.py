#!/usr/bin/env python
import re
import Image

i = Image.open("data/oxygen.png")
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
shades = [r for r, g, b, a in row if r == g == b] #grey squares are equal amounts of rgb

# convert to chars and join
# print "".join(map(chr,shades))

# get new values
# print map(int, re.findall("\d+", "".join(map(chr, shades))))
print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, shades))))))