from PIL import Image

#img = Image.open('pixels.png')
img = Image.open('TV.png').convert("RGB")
pixels = list(img.getdata())

flag = ''
for px in pixels:
    for val in px:
        flag += chr(val)

print(repr(flag))
