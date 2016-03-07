#!/usr/bin/python

import Image
import sys
import argparse


parser = argparse.ArgumentParser(description='Used to transpose the colors in an image.')
parser.add_argument('filename', type=str, help='The file to be transposed')
parser.add_argument('change', type=str, choices=["rbg", "grb", "gbr", "brg", "bgr"], help="the colors to be transposed")
parser.add_argument("--outfile", type=str, required=False, help="The file to output to")

args = parser.parse_args()

infile = Image.open(args.filename)
r, g, b = infile.split()

if (args.change=="rbg"):
  outpic = Image.merge("RGB", (r, b, g))
elif (args.change=="grb"):
  outpic = Image.merge("RGB", (g, r, b))
elif (args.change=="gbr"): 
#  print "gbr"
#  outpic = Image.merge("RGB", (g, b, r))
  outpic = Image.merge("RGB", (b, r, g))

elif (args.change=="brg"): 
#  print "brg"
#  outpic = Image.merge("RGB", (b, r, g))
  outpic = Image.merge("RGB", (g, b, r))

elif (args.change=="bgr"):
  outpic = Image.merge("RGB", (b, g, r))


if (args.outfile == None):
  dotpos = args.filename.rfind(".")
  basename = args.filename[0:dotpos]
  extension = args.filename[dotpos+1:]
  outfile = basename + "_mod." + extension
else:
  outfile = args.outfile

outpic.save(outfile)
