#!/usr/bin/env python
import urllib,contextlib
import pickle

def main():
    with contextlib.closing(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")) as handle:
        data = pickle.load(handle)

    # pairs of characters and numbers of times printed
    for line in data:
        print "".join(i[1]*i[0] for i in line)

if __name__ == "__main__":
    main()