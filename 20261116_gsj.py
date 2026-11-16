from machine import Pin
import time

flash = Pin(4, Pin.OUT)
flash.value(0)

print("BOOT OK")

while True:
    flash.value(1)
    print("ON")
    time.sleep(1)
    flash.value(0)
    print("OFF")
    time.sleep(1)