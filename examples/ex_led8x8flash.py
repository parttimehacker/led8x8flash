#!/usr/bin/python3
""" Example of the Flash 8x8 LED matrix dispplay class """

from threading import Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

from led8x8flash.led8x8flash import Led8x8Flash

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = BicolorMatrix8x8.BicolorMatrix8x8()
    FLASH = Led8x8Flash(DISPLAY, LOCK, 1, 0.5)
    FLASH.reset()
    for test in range(10):
        FLASH.display()
    FLASH.set_color(2)
    for test in range(10):
        FLASH.display()
    FLASH.set_color(3)
    for test in range(10):
        FLASH.display()