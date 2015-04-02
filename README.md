Scripts and programs I use on my Rspberry Pi.
Most of them rely on [wiringPi](http://wiringpi.com) to be used as a regular
user (no need to be root). All of them are "one-shots" run by *cron*.

- **7seg**: Python scripts to play with a 7-segment display. Use Adafruit's
  [LED Backpack library](https://github.com/adafruit/Adafruit_Python_LED_Backpack)
  - **7seg/7seg_init.py**: "boots" the display
  - **7seg/7seg_loop.py**: test script. Turn segments on and off consecutively
  - **7seg/7seg_set.py**: writes a string or number to the display
- **dht**: C sources for a program to get readings from a DHT sensor. Using
  part of Adafruit's [Python DHT driver](https://github.com/adafruit/Adafruit_Python_DHT)
  code, keeping only relevant code.
  Compile it, set its sticky bit to root and put somewhere in your *PATH*
- **4017.sh**: script used to control an IC4017.
- **blind.sh**: acts on a VELUX roller shutter remote connected to the Pi
- **blind_down_check.py**: returns if the shutter should be closed (at night)
- **crontab**: self-explanatory
- **dht_graph.py**: creates a graph of temperature and humidity for a given
  period with *rrdtool*.
- **dht_scripts.sh**: reads from the DHT sensor and updates the 7-segment
  display and IC4017-controled bargraph
- **gmail_unread_count.py**: prints the number of unread mails
- **theoldreader_unread_count.py**: prints the number of unread articles on TheOldReader

