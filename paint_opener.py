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
        chunks = [struct.unpack(STRUCT_FMT, chunk) for chunk in read_chunks(f)]
    
    return chunks

def draw(filename: str):
    content = load(filename=filename)
    width = StellarUnicorn.WIDTH
    height = StellarUnicorn.HEIGHT

    pixels = [content[i:i+width] for i in range(0, len(content), width)]

    for i in range(width):
        for j in range(height):
            b, g, r = pixels[i][j]
            graphics.set_pen(graphics.create_pen(r, g, b))
            graphics.pixel(i, j)
