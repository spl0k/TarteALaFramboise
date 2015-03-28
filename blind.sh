#!/bin/sh

GPIO=/usr/local/bin/gpio

BUTTON_UP=21
BUTTON_STOP=20
BUTTON_DOWN=16

button_press()
{
	$GPIO -g mode $1 output
	$GPIO -g write $1 0
	$GPIO -g mode $1 input
}

case $1 in
	up)
		button_press $BUTTON_UP
		echo $1 >/tmp/blind_state
		;;
	down)
		button_press $BUTTON_DOWN
		echo $1 >/tmp/blind_state
		;;
	stop)
		button_press $BUTTON_STOP
		;;
	*)
		echo "Usage: $0 {up|down|stop}"
		exit 1
		;;
esac

