#!/usr/bin/env python
from re import findall

with open("./data/equality.txt",'r') as f:
    data=f.read()

print "".join(findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))
