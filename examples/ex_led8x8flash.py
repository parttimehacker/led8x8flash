#!/usr/bin/python3
""" Example of the Flash 8x8 LED matrix dispplay class """

import threading

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

import led8x8flash

if __name__ == '__main__':
    LOCK = threading.Lock.Lock()
    DISPLAY = BicolorMatrix8x8()
    FLASH = led8x8flash.Led8x8Flash(MATRIX, LOCK, 2, 1.0)
    FLASH.reset()
    while True:
    	FLASH.display()

