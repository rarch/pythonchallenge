#!/usr/bin/env python
from re import findall
from util import fread

def main():
    data=fread("./data/ocr.txt")

    print "".join(findall("[A-Za-z]", data))

if __name__ == "__main__":
    main()