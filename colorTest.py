from __future__ import division
import time

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
# SPI_PORT   = 
# SPI_DEVICE = 
# pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))



pixels.clear()
for i in range(PIXEL_COUNT):
    pixels.set_pixel_rgb(i , 88, 88, 88) 

   
pixels.show()