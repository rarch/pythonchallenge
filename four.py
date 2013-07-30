#!/usr/bin/env python
from re import search
from urllib import urlopen

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing_rep = "and the next nothing is (\d+)"
# nothing = "12345"
nothing = "8022" #"Yes. Divide by two and keep going."

while True:
    try:
        source = urlopen(uri % nothing).read()
        nothing = search(nothing_rep, source).group(1)
    except:
        print source
        break
    # print nothing