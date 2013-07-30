#!/usr/bin/env python
from re import search
import collections
import zipfile

# comments, num, fn = [], "90052", "data/channel/%s.txt"
next = "Next nothing is (\d+)"
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

myzip = zipfile.ZipFile("data/channel.zip")
comments, num, fn = [], "90052", "%s.txt"

while True:
    try:
        num = search(next, myzip.read(fn % num)).group(1)
    except:
        print myzip.read(fn % num)
        break

    newc=myzip.getinfo(fn % num).comment
    if newc not in comments and newc.isalpha():
        comments.append(newc)
    # comments.append(myzip.getinfo(fn % num).comment)

# print comments
print "".join(comments)