#!/usr/bin/env python
import pyqrcode
from PIL import Image
import numpy as np

def xorstr(xs, ys):
	return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(xs, ys))

def make_qr(data, version=4):
	qr = pyqrcode.QRCode(data, version=version)
	text = qr.text(quiet_zone=1)
	return [map(int, row) for row in text.split()]

flag  = open("flag.txt").read().strip()
hint1 = "Sorry, it's not quite that easy..."
hint2 = "Maybe try combining these hints..."
junk  = xorstr(flag, xorstr(hint1, hint2))
rgb   = (hint1, hint2, junk)
qrgb  = np.dstack(map(make_qr, rgb))
orig  = Image.open("mrrobot.jpg")
stego = orig.copy()

def set_low_bit(*args):
	val, low_bit = args
	return (val & ~1) | (1 - low_bit)

for x in range(stego.size[0]):
	for y in range(stego.size[1]):
		orig_px = stego.getpixel((x, y))
		hide_px = qrgb[y // 10][x // 10]
		stego.putpixel((x, y), tuple(map(set_low_bit, orig_px, hide_px)))

stego.save("attachments/HelloFriend.png")
