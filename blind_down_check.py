#!env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import os.path, sys
import time

cur_time = time.localtime()

update_sunset_time = False
if not os.path.exists('/tmp/sunset'):
	update_sunset_time = True
elif time.localtime(os.path.getmtime('/tmp/sunset')).tm_yday != cur_time.tm_yday:
	update_sunset_time = True

if update_sunset_time:
	r = requests.get("http://www.timeanddate.com/sun/france/paris")
	bs = BeautifulSoup(r.text)
	tag = bs.select("tr.hl td:nth-of-type(10)")[0]
	sunset = tag.string.replace(' h ', ':')

	with open('/tmp/sunset', 'w') as f:
		f.write(sunset)
else:
	with open('/tmp/sunset', 'r') as f:
		sunset = f.read()

state = 'unknown'
if os.path.exists('/tmp/blind_state'):
	with open('/tmp/blind_state') as f:
		state = f.read()
state = state.strip()

if state == 'down':
	sys.exit(1)

hour, minute = map(int, sunset.split(':'))
if hour < cur_time.tm_hour or (hour == cur_time.tm_hour and minute <= cur_time.tm_min):
	sys.exit(0)

sys.exit(1)

