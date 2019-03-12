from PIL import Image

flag = 'DCI{p1c7ur35_c4n_74lk_700!!}'

print(len(flag))

hexes = [ord(x) for x in flag*12000]

pixels = []

for p in range(0, len(hexes), 3):
    pixels.append((hexes[p], hexes[p+1], hexes[p+2]))
print(len(pixels))
img = Image.new("RGB", (500,224))
img.putdata(pixels)
img.save("pixels.png")
