import struct
from stellar import StellarUnicorn

STRUCT_FMT = 'BBBx'
STRUCT_LEN = struct.calcsize(STRUCT_FMT)

graphics = None

def read_chunks(f):
    while True:
        chunk = f.read(STRUCT_LEN)
        if not chunk:
            break
        yield chunk

def load(filename: str):
    with open(f"saves/{filename}.bin", mode="rb") as f:
        chunks = [list(reversed(struct.unpack(STRUCT_FMT, chunk))) for chunk in read_chunks(f)]
    
    return chunks

def draw(filename: str):
    content = load(filename=filename)

    for i in range(StellarUnicorn.HEIGHT):
        for j in range(StellarUnicorn.WIDTH):
            r, g, b = content[j * StellarUnicorn.WIDTH + i]
            graphics.set_pen(graphics.create_pen(r, g, b))
            graphics.pixel(i, j)
    return content

if __name__ == "__main__":
    from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN
    stellar = StellarUnicorn()
    graphics = PicoGraphics(DISPLAY_STELLAR_UNICORN)

    draw(filename="calibration")

    stellar.update(graphics)