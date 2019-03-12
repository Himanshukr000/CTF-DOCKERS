#!/usr/bin/python
from PIL import Image

f = open("nonlinear2.txt")
hexdump = f.read().replace("\n", "")

value = bin(int(hexdump, 16))[2:]
value = "0"*(len(hexdump)*4 - len(value)) + value

print("Bits: %d" % len(value))

cmap = {'0': (255,255,255),
        '1': (0,0,0)}

data = [cmap[letter] for letter in value]
img = Image.new('RGB', (32, 27), "white")
img.putdata(data)
img.show() 
