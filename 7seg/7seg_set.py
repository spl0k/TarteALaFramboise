#!env python
# coding: utf-8

import sys
import argparse
from Adafruit_LED_Backpack.SevenSegment import SevenSegment

parser = argparse.ArgumentParser()
parser.add_argument("value")
parser.add_argument("-n", "--numeric", action = "store_true")
parser.add_argument("-p", "--precision", type = int)
args = parser.parse_args()

display = SevenSegment()
display.clear()

if args.numeric:
	try:
		fvalue = float(args.value)
	except ValueError:
		parser.print_usage()
		print >>sys.stderr, "{}: error: invalid numeric value '{}'".format(sys.argv[0], args.value)
		sys.exit(1)

	if args.precision is not None:
		display.print_float(fvalue, args.precision)
	else:
		display.print_number_str(str(fvalue))
else:
	display.print_number_str(args.value)

display.write_display()

