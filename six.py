#!/usr/bin/env python
from re import search
import collections
import zipfile

next = "Next nothing is (\d+)"

# look through all files
# comments, num, fn = [], "90052", "data/channel/%s.txt"
# while True:
#     try:
#         with open(fn%num,"r") as f:
#             # contents = f.read()
#             num = search(next,f.read()).group(1)
#             # num = search(next,contents).group(1)
#     except:
#         break
#     # print contents

# with open(fn%num,"r") as f:
#     print f.read()

# process zip file
myzip = zipfile.ZipFile("data/channel.zip")
comments, num, fn = [], "90052", "%s.txt"

while True:
    try:
        num = search(next, myzip.read(fn % num)).group(1)
    except:
        # last file, so print contents
        # print myzip.read(fn % num)
        break

    # get the comments, as instructed

    # append comments
    # comments.append(myzip.getinfo(fn % num).comment)

    # oxygen did not work
    # instead only append alphabetic, and only once
    newc=myzip.getinfo(fn % num).comment
    if newc not in comments and newc.isalpha():
        comments.append(newc)

# print comments
print "".join(comments)