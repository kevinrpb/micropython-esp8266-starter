from machine import Pin

def pin_id(pin: Pin) -> int:
  id_str = str(pin)[4:-1].rstrip(",")
  id_int = int(id_str)

  return id_int
