from __future__ import division
import time

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 160
PIXEL_CLOCK = 13
PIXEL_DOUT  = 6

pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

while True:
    for i in range(PIXEL_COUNT-3):
        pixels.clear()
        pixels.set_pixel_rgb(i, 255, 0, 0) 
        pixels.set_pixel_rgb(i + 1, 255, 0, 0) 
        pixels.set_pixel_rgb(i + 2, 0, 255, 0) 
        pixels.set_pixel_rgb(i + 3, 0, 255, 0)  
        pixels.show()
    for i in range(PIXEL_COUNT-1, 3, -1):
        pixels.clear()
        pixels.set_pixel_rgb(i , 0, 255, 0) 
        pixels.set_pixel_rgb(i - 1, 0, 255, 0) 
        pixels.set_pixel_rgb(i - 2, 255, 0, 0) 
        pixels.set_pixel_rgb(i - 3, 255, 0, 0) 
        pixels.show()