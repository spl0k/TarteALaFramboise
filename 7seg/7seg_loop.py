#!env python
# coding: utf-8

from Adafruit_LED_Backpack.SevenSegment import SevenSegment
import time

display = SevenSegment()

i0 = 0
i1 = 0
i2 = 0
i3 = 0
c = False
while True:
	display.set_digit_raw(0, i0)
	display.set_digit_raw(1, i1)
	display.set_digit_raw(2, i2)
	display.set_digit_raw(3, i3)
	display.set_colon(c)
	display.write_display()
	i0 = (i0+1) & 0xFF
	if not i0 % 2:
		i1 = (i1+1) & 0xFF
	if not i0 % 3:
		i2 = (i2+1) & 0xFF
	if not i0 % 4:
		i3 = (i3+1) & 0xFF
	if not i0 % 5:
		c = not c
	time.sleep(0.2)
