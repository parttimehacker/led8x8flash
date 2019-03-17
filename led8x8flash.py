#!/usr/bin/python3
""" Display full screen flash color pattern on an Adafruit 8x8 LED backpack """

import time

BRIGHTNESS = 5

UPDATE_RATE_SECONDS = 0.2

PING = 0
PONG = 1

class Led8x8Flash:
    """ flash pattern based on color and time interval  """

    def __init__(self, matrix8x8, lock, color):
        """ create initial conditions and saving display and I2C lock """
        self.matrix = matrix8x8
        self.matrix.begin()
        self.bus_lock = lock
        self.alternate = PING
        if color < 0:
            self.color = 0
            raise Exception('color should be greater than 0 The value of color was: {}'.format(x))
        elif color > 3:
            self.color = 3
            raise Exception('color should not be greater than 3 The value of color was: {}'.format(x))
        else:
            self.color = color

    def reset(self,):
        """ initialize to starting state and set brightness """
        self.bus_lock.acquire(True)
        self.alternate = PINGS)
        self.bus_lock.release()

    def set_color(self, color):
        """ initialize to starting state and set brightness """
        self.bus_lock.acquire(True)
        if color < 0:
            self.color = 0
            raise Exception('color should be greater than 0 The value of color was: {}'.format(x))
        elif color > 3:
            self.color = 3
            raise Exception('color should not be greater than 3 The value of color was: {}'.format(x))
        else:
            self.color = color
        self.bus_lock.release()

    def display(self,):
        """ display the series as a 64 bit image with alternating colored pixels """
        time.sleep(UPDATE_RATE_SECONDS)
        self.bus_lock.acquire(True)
        if self.alternate == PING:
            self.alternate = PONG
        else:
            self.alternate = PING
        for xpixel in range(0, 8):
            for ypixel in range(0, 8):
                if self.alternate == PING:
                    self.matrix.set_pixel(xpixel, ypixel, self.color)
                else:
                    self.matrix.set_pixel(xpixel, ypixel, 0)
        self.matrix.write_display()
        self.bus_lock.release()

if __name__ == '__main__':
    exit()
