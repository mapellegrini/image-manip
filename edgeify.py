#!/usr/bin/python

import Image
import math
import sys
import copy
import argparse

def dist(tup1, tup2): 
#takes two tuples representing 3d coordinates (pixels)
#returns the distance between them 
  xdist = tup1[0]-tup2[0]
  ydist = tup1[1]-tup2[1]
  zdist = tup1[2]-tup2[2]
  return int(math.sqrt(1.0/3 * xdist*xdist + ydist*ydist + zdist*zdist))


parser = argparse.ArgumentParser(description='Isolate the edges in an image.')
parser.add_argument('--threshold', metavar='t', dest='thresh', type=int,
                   help='The threshold value for detecting an edge (0-255). Default value is 20')
parser.add_argument('--save', action='store_true', help='Output the intermediate black-and-white image')
parser.add_argument('filename', type=str, help='The file to be processed')

args = parser.parse_args()
#parser.print_help()

if (args.thresh is None):
  thresh = 20
elif (args.thresh < 0 or args.thresh > 255):
  print "ERROR! Threshold must be betwen 0 and 255 inclusive"
  sys.exit(5)  
else:
  thresh=args.thresh


img = Image.open(args.filename)
pixels = img.load()

cpixels = [] #for storing a temporary copy of the pic
print "Convert pic to black and white"
for i in range(img.size[0]):
  cpixels.append([])
  for j in range(img.size[1]):
    val = dist(pixels[i,j], (0,0,0))
    pixels[i,j]=(val, val, val)
    cpixels[i].append((val, val, val)) 

if (args.save):
  img.save("bw_" + args.filename, "JPEG")

print "Detecting edges"
for i in range(1, img.size[0]-1):
  for j in range(1, img.size[1]-1):
    myval = cpixels[i+0][j+0][0]
    lval  = cpixels[i-1][j+0][0]
    rval  = cpixels[i+1][j+0][0]
    uval  = cpixels[i+0][j-1][0]
    dval  = cpixels[i+0][j+1][0]

    if (abs(myval-lval) > thresh or abs(myval-rval) > thresh or abs(myval-uval) > thresh or abs(myval-dval) > thresh):
      pixels[i,j]=(myval, myval, myval)
    else:
      pixels[i,j]=(255,255,255)

#img.show()
#img.save("edge_" + args.filename, "JPEG")
img.save("edge_" + args.filename)
