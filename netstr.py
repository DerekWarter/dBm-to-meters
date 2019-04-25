import subprocess as sp
from time import sleep
import re
from math import log10

while(True):
	sp.call('clear')
	out = sp.check_output(["iwconfig", "wlan0"])
	out = out.decode("utf-8")
	filt = re.search("(?:Signal level=)([+-][0-9]+)",out)
	dBm = int(filt.group(1))
	MHz = 2417
	FSPL = 27.55
	dist = 10 ** ((FSPL - (20 * log10(MHz)) + abs(dBm)) / 20)
	dist = round(dist, 2)
	print("WIFI SIGNAL STRENGTH TRACKER: \n")
	print("SIG STRENGTH: ", dBm)
	print("PREDICTED DISTANCE (m): ", dist)
	sleep(1)
