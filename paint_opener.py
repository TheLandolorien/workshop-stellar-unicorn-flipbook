from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN

FILENAME = "triangle4"

su = StellarUnicorn()
graphics = PicoGraphics(display=DISPLAY_STELLAR_UNICORN)

with open(f"saves/{FILENAME}.bin", mode="rb") as f:
    image_data = f.read()
    
for i in range(len(image_data), 0, -4):
    r, g, b, _ = image_data[i - 4:i]
    # print(f"{i}: ({(len(image_data) - i) // 64}, {(len(image_data) - i) // 4 % 16}) => ({r}, {g}, {b})")
    graphics.set_pen(graphics.create_pen(r, g, b))
    graphics.pixel((len(image_data) - i) // 64, (len(image_data) - i) // 4 % 16)

su.update(graphics)
