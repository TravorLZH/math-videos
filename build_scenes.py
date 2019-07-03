#!/usr/bin/env python3
import sys
import os

# It is not supposed to be imported
assert(__name__=="__main__")

argc=len(sys.argv)

quality_to_arg={
    "1440p60":"",   # Default
    "720p30":"-m",  # Medium quality
    "480p15":"-l"   # Low quality
}

acceptable_argv1=quality_to_arg.keys()

if argc<2:
    print("usage: %s %s" % (sys.argv[0],'|'.join(acceptable_argv1)))
    exit(-1)

if sys.argv[1] not in acceptable_argv1:
    print("error: unknown video quality `%s'" % sys.argv[1])

src="scenes.py"

assert(os.path.exists(src)==True)   # Make sure the file is available
listfile=open("list.txt","r")
classes=[]
while True:
    line=listfile.readline()
    if not line:
        break
    classes.append(line.split('.')[0].split(' ')[1])
os.system("manim %s %s %s" % (quality_to_arg[sys.argv[1]],
    src,' '.join(classes)))

print("Build Complete")
