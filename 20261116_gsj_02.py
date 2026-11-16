from machine import Pin
import time

flash = Pin(4, Pin.OUT)
flash.value(0)

print("BOOT OK")

try:
    while True:
        flash.value(1)
        time.sleep(2)
        flash.value(0)
        time.sleep(2)
    
except KeyboardInterrupt:
    flash.value(0)
    print("종료합니다.")
