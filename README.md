# dBm-to-meters
Very short script to convert 2.4 GHz WiFi signal strength reading (in decibels per milliwatt) to distance from hotspot in meters.

Uses free-space path loss to approximate distance to a connected hotspot, assuming the transmitter is a mid-grade consumer/office device.
To use, simply run the script through the Python interpreter. Script assumes wireless LAN device is labelled wlan0.
