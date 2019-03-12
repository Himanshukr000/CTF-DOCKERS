#!/usr/bin/env python

import base64
import sys
from Crypto.Cipher import AES

key = "I_AM_THE_FALLOUT"
iv  = "WHAT_IN_THE_BOOM"
pad_size = 16


def decrypt(msg):
    if len(msg) % pad_size != 0:
        raise Exception("Incorrect message length")
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(msg)


def unpad(data, block_size):
    if len(data) % block_size != 0:
        raise Exception("Incorrect message length")
    must_unpad = ord(data[-1])
    if must_unpad < 0 or must_unpad > block_size:
        raise Exception("Incorrect padding")
    if data[-must_unpad:] != chr(must_unpad) * must_unpad:
        raise Exception("Incorrect padding")
    return data[:-must_unpad]


if __name__ == "__main__":
    try:
        line = base64.b64decode(raw_input())
        try:
            line = decrypt(line)
            data = unpad(line, pad_size)
            print "Correct padding"
        except Exception, msg:
            print msg
    except:
        print "Incorrect formatting!"
