#!/usr/bin/env python
from re import findall
from util import fread

def main():
    data=fread("./data/equality.txt")

    print "".join(findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))

if __name__ == "__main__":
    main()