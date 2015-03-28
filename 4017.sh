#!/bin/sh

GPIO=/usr/local/bin/gpio

if [ $# -lt 3 ]; then
	echo "Usage: $0 <clock-pin> <reset-pin> <value>"
	exit 1
fi
if [ $3 -lt 1 -o $3 -gt 10 ]; then
	echo "Usage: $0 <clock-pin> <reset-pin> <value>"
	echo "  <value> should be between 1 and 10 (inclusive)"
	exit 1
fi

$GPIO -g write $2 1
$GPIO -g write $2 0
for i in $(seq $(($3 - 1))); do
	$GPIO -g write $1 1
	$GPIO -g write $1 0
done

exit 0

