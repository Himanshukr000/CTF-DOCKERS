#!/usr/bin/env python

import sys
import mysocket
import base64
from Crypto.Cipher import AES
import random

iv  = "WHAT_IN_THE_BOOM"
pad_size = 16

host = ""
port = 0

def encrypt(msg):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(msg)


def randbytes(num):
    return bytearray("".join([chr(random.randint(0,255)) for _ in range(num)]))


def oracle(ciphertext):
    ciphertext = base64.b64encode(ciphertext)
    sock = mysocket.mysocket(host, port)
    sock.sendline(ciphertext)
    recv = sock.recvline().lower()
    print ciphertext, recv
    return "correct" in recv and not "incorrect" in recv


def find_pad(block, attack, index):
    for i in range(256):
        attack[index] = i
        ciph = attack + block
        poss = oracle(ciph)
        if poss:
            return i
    return None


def find_block(cur_block, prev_block):
    plaintext = randbytes(pad_size)
    attack = randbytes(pad_size)
    for place in range(pad_size - 1, -1, -1):
        pad = pad_size - place
        for i in range(pad_size - 1, place, -1):
            # C'[i] = pad ^ Pn[i] ^ Cn-1[i]
            attack[i] = pad ^ plaintext[i] ^ prev_block[i]
        val = find_pad(cur_block, attack, place)
        # Pn[place] = pad ^ Cn-1[place] ^ C'[place]
        plaintext[place] = pad ^ prev_block[place] ^ val
    return plaintext


def padding_oracle_attack(ciphertext):
    plaintext = bytearray(b"")
    msg = len(ciphertext)
    for i in range(msg - pad_size, pad_size - 1, -pad_size):
        cur_block = ciphertext[i:i + pad_size]
        prev_block = ciphertext[i - pad_size:i]
        block = find_block(cur_block, prev_block)
        plaintext = block + plaintext
    return plaintext


if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print "Usage:"
        print "%s <host> <port>" % sys.argv[0]
        sys.exit(0)
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except:
        print "second argument must be an int!"

    
    with open("msg.txt") as filein:
        msg = bytearray(base64.b64decode(filein.read().strip()))
    
    print padding_oracle_attack(bytearray(iv) + msg)
