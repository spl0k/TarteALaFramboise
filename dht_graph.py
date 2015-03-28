#!env python
# coding: utf-8

import subprocess, argparse
import string, math
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("rrdtool")
parser.add_argument("rrdb")
parser.add_argument("out")
parser.add_argument("-s", "--start", default = "end-1day")
parser.add_argument("-e", "--end", default = "now")
args = parser.parse_args()

timestamps = []
temperatures = []
humidities = []

proc = subprocess.Popen(
	[ args.rrdtool, "fetch", args.rrdb, "AVERAGE", "--start", args.start, "--end", args.end ],
	env = { "LC_NUMERIC": "C" },
	stdout = subprocess.PIPE)
for line in iter(proc.stdout.readline, ''):
	line = line.rstrip()
	if not line or line[0] in string.whitespace:
		continue

	split = line.split()
	timestamps.append(int(split[0].translate(None, ':')))
	temperatures.append(float(split[1]))
	humidities.append(float(split[2]))

proc.wait()

min_bound = math.floor(min(filter(lambda f: not math.isnan(f), temperatures)) * 0.5) * 2
max_bound = math.ceil( max(filter(lambda f: not math.isnan(f), temperatures)) * 0.5) * 2
scale = 100.0 / (max_bound - min_bound)

graph_cmd = [
	args.rrdtool, "graph", args.out, "--slope-mode",
	"--width", "720", "--height", "270",
	"--start", args.start, "--end", args.end,
	"--upper-limit", str(max_bound), "--lower-limit", str(min_bound), "--rigid",
	"--y-grid", "1:2", #"--left-axis-format", "%.0lf°C",
	"--right-axis", "{}:-{}".format(scale, min_bound * scale),
	"--right-axis-format", "%3.0lf%%",
	"DEF:temp={}:temperature:AVERAGE".format(args.rrdb),
	"DEF:humi={}:humidity:AVERAGE".format(args.rrdb),
	"CDEF:shumi=humi,{1},{0},-,100,/,*,{0},+".format(min_bound, max_bound),
	"LINE1.5:temp#00FF00:Temperature",
	"LINE1.5:shumi#0000FF:Humidity",
	"--watermark", "From {} to {}".format(
		datetime.fromtimestamp(timestamps[0]).strftime("%Y-%m-%d"),
		datetime.fromtimestamp(timestamps[-1]).strftime("%Y-%m-%d"))
]

with open('/dev/null', 'w') as devnull:
	proc = subprocess.Popen(graph_cmd, stdout = devnull)
	proc.communicate()
	proc.wait()

