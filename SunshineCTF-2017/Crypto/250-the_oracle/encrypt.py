#!/usr/bin/python

import sys
import base64
from Crypto.Cipher import AES

key = "I_AM_THE_FALLOUT"
iv  = "WHAT_IN_THE_BOOM"
pad_size = 16

# msg = "MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc="
# msg = "sun{I_b3t_Th3_0r4cL3_c0uLDNt_Pr3d1cT_Th3_f4110uT}"
with open("flag.txt", "r") as flagfile:
    msg = flagfile.read().strip()

def make_pad(size):
    return chr(size) * size


def pad_block(block, pad_size):
    dif = pad_size - len(block)
    barray = block
    return "".join([barray, make_pad(dif)])


def pad(data, block_size):
    ending = make_pad(block_size - (len(data) % block_size))
    return "".join([data, ending])

if __name__ == "__main__":
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = msg
    print plain
    plain = pad(plain, pad_size)
    line = cipher.encrypt(plain)
    b64 = base64.b64encode(line)
    print b64
