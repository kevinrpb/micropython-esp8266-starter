import network

import config

_station = None
_station = network.WLAN(network.STA_IF)

def connect():
  global _station

  if not _station.isconnected():
    _station.active(True)
    _station.connect(config.WIFI_SSID, config.WIFI_PASS)

    while not _station.isconnected():
      pass

def get_station():
  return _station
