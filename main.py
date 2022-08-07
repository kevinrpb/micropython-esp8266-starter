import time
import time

import config

import util.log as log
import util.wifi as wifi
from sketch import loop, setup

# This here is just a naive way of making the console output not appear together with
# the gibberish that shows up when the board boots
print('')
print('')
print('')

if config.WIFI_ENABLED:
  log.debug('Connecting wifi')
  wifi.connect()

log.debug('Running `setup()`')
setup()

_starttime = time.time()
while True:
  log.debug('Running `loop()`')
  loop()

  time.sleep(config.LOOP_DELAY - ((time.time() - _starttime) % config.LOOP_DELAY))
