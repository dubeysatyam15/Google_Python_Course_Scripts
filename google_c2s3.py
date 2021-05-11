#!/usr/bin/env python3
import os

# We want to make use of listdir(), path.join(), path.isdir() methods of OS MODULE
dir = "/home/ubuntu"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
