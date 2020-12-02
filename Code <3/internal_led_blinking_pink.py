import time
import board

import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    print ("make it bubblegum!")
    dot.fill((255, 0, 255))
    time.sleep(1)
    print ("make it magenta!")
    dot.fill((255, 0, 102))
    time.sleep(1)