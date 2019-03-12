#!/usr/bin/env python

from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random
import sys

p = getPrime(512)
q = getPrime(512)
n = p * q
n2 = n ** 2
l = (p - 1) * (q - 1)
mu = inverse(l, n)

flag = bytes_to_long(open('flag').read())

r = random.randint(1, n)
c = (pow(n + 1, flag, n2) * pow(r, n, n2)) % n2

print 'n = %d' % n
print 'encrypted_flag = %d' % c
print 'What do you want to decrypt?'

sys.stdout.flush()

data = int(raw_input())

if data == c:
    print 'You tried ;)'
else:
    output = (((pow(data, l, n2) - 1) / n) * mu) % n

    print 'output = %d' % output

sys.stdout.flush()
