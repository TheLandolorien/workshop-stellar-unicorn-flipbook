graphics = None

def load(filename: str):
    with open(f"saves/{filename}.bin", mode="rb") as f:
        image_data = f.read()
    
    return image_data

def draw(filename: str):
    image = load(filename=filename)
    for i in range(len(image), 0, -4):
        r, g, b, _ = image[i - 4:i]
        graphics.set_pen(graphics.create_pen(r, g, b))
        graphics.pixel((len(image) - i) // 64, (len(image) - i) // 4 % 16)
