#
# CircuitPython code
# Supported on Gemma M0
# There is no machine API on Atmel SAMD21 port - https://circuitpython.readthedocs.io/en/3.x/docs/ 
# CircuitPython doesn't support interrupts?  WTF?
#

import digitalio, board, adafruit_dotstar
from time import sleep
from touchio import TouchIn

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
dot[0] = (0,0,0)

led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT

def main():
    led_on = dot_on = True
    touch0 = TouchIn(board.A0)
    touch2 = TouchIn(board.A2)
    while True:
        if touch0.value:
            if led_on:
                print("Turn Off")
                led_on = False
            else:
                print("Turn On")
                led_on = True
        led.value = led_on
        if touch2.value:
            if dot_on:
                print("Turn Off")
                dot_on = False
                dot[0] = (0,0,0)
            else:
                print("Turn On")
                dot_on = True
                dot[0] = (0xFF,0x14,0x93)
        sleep(0.2)