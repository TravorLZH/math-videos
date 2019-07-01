#!/usr/bin/env python3
import sys
import os

# It is not supposed to be imported
assert(__name__=="__main__")

src="scenes.py"

assert(os.path.exists(src)==True)   # Make sure the file is available
listfile=open("list.txt","r")
classes=[]
while True:
    line=listfile.readline()
    if not line:
        break
    classes.append(line.split('.')[0].split(' ')[1])
os.system("manim %s %s" % (src,' '.join(classes)))

print("Build Complete")
