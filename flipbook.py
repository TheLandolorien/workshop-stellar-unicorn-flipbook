import time

import pngdec
from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN

NUM_FRAMES = 4
FLIPBOOK_NAME = ""

su = StellarUnicorn()
graphics = PicoGraphics(display=DISPLAY_STELLAR_UNICORN)

p = pngdec.PNG(graphics)

n = 0
while True:
    if n > NUM_FRAMES:
        n = 0

    p.open_file(f"{FLIPBOOK_NAME}_{n}.png")
    p.decode(0, 0)

    time.sleep(1)
    su.update(graphics)

    n += 1
