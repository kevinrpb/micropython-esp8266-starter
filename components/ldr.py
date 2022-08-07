from machine import ADC, Pin

from util.pin import pin_id

class LDR:
  def __init__(self, pin, min_value=0, max_value=1024):
    if min_value >= max_value:
      raise Exception('Min value is greater or equal to max value')

    # initialize ADC (analog to digital conversion)
    if isinstance(pin, int):
      self.adc = ADC(pin)
    elif isinstance(pin, Pin):
      self.adc = ADC(pin_id(pin))
    else:
      raise Exception('Couldn\'t get pin ID')

    # Only for ESP32
    # self.adc.atten(ADC.ATTN_11DB)

    self.min_value = min_value
    self.max_value = max_value

  def read(self):
    return self.adc.read()

  def value(self):
    in_min = self.min_value
    in_max = self.max_value

    out_min = 0.0
    out_max = 1.0

    x_analog = self.read()
    x_mapped = (x_analog - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    return 1 - x_mapped
