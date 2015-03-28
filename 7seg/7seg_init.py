#!env python
# coding: utf-8

import argparse
from Adafruit_LED_Backpack.SevenSegment import SevenSegment

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--brightness", type = int, default = 15)
args = parser.parse_args()

display = SevenSegment()
display.begin()
display.set_brightness(args.brightness)

