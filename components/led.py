class LED:
  def __init__(self, pin):
    self.pin = pin

  def on(self):
    self.pin.on()

  def off(self):
    self.pin.off()

  def toggle(self):
    self.pin.toggle()
