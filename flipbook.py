import time
import paint_opener

NUM_FRAMES = 2
FLIPBOOK_NAME = "cross"
SPEED = 0.125 # Second(s)

graphics = None
n = 1

def init():
    paint_opener.graphics = graphics

def draw():
    global n
    if n > NUM_FRAMES:
        n = 1
    paint_opener.draw(filename=f"{FLIPBOOK_NAME}_{n}")

    time.sleep(SPEED)

    n += 1

if __name__ == '__main__':
    from stellar import StellarUnicorn
    from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN
    stellar = StellarUnicorn()
    graphics = PicoGraphics(DISPLAY_STELLAR_UNICORN)
    while True:
        init()
        draw()
        stellar.update(graphics)