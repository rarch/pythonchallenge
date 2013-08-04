#!/usr/bin/env python
from re import search
from urllib import urlopen

def main():
    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    nothing_rep = "and the next nothing is (\d+)"
    nothing = "12345"
    source=""

    while True:
        try:
            source = urlopen(uri % nothing).read()
            nothing = search(nothing_rep, source).group(1)
        except:
            print source
            break
        # print nothing

def main_two():
    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    nothing_rep = "and the next nothing is (\d+)"
    nothing = "8022" #"Yes. Divide by two and keep going."
    source=""

    while True:
        try:
            source = urlopen(uri % nothing).read()
            nothing = search(nothing_rep, source).group(1)
        except:
            print source.split(".")[0]    # print source
            break
        # print nothing

if __name__ == "__main__":
    # main()
    main_two()