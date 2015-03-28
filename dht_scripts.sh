#!/bin/sh

DHT=/usr/local/bin/dht
RRDTOOL=/usr/bin/rrdtool
PYTHON=/usr/bin/python

dht_result=$($DHT -s 22 $1 5)

$RRDTOOL update /home/spl0k/dht.rrd N:$(echo $dht_result | sed 's/ /:/')
$PYTHON /home/spl0k/7seg/7seg_set.py -np1 $(echo $dht_result | cut -d' ' -f1)
/home/spl0k/4017.sh $2 $3 $(echo $dht_result | cut -d' ' -f2 | cut -b1)

