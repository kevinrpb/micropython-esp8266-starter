import pins
import util.log as log
from components import LDR, LED

ldr_sensor = None
led_diode = None

def setup():
  global ldr_sensor, led_diode

  ldr_sensor = LDR(pins.ldr, min_value=0, max_value=1024)
  led_diode = LED(pins.internal_led)

def loop():
  light_value = ldr_sensor.value()
  log.info(f'Light value: {light_value:.4f}')

  if light_value < 0.5:
    led_diode.off()
  else:
    led_diode.on()
