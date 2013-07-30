#!/usr/bin/env python
from re import findall

with open("./data/ocr.txt",'r') as f:
    data=f.read()
print "".join(findall("[A-Za-z]", data))