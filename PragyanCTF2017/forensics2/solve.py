# coding: utf-8
from PIL import Image
im = Image.open('transmission.png')
pixels = list(im.getdata())
        
for i,p in enumerate(pixels):
    if p[3] == 0:
        pixels[i] = (p[0], p[1], p[2], 255)
        
        
im.putdata(pixels)
im.save('output.png')
