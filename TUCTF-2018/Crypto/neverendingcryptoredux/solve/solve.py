#!/usr/bin/env python2

import sys

from pwn import *

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE_DICT = dict((v,k) for k,v in MORSE_CODE_DICT.iteritems())

def level_zero_decrypt(enc):
    global MORSE_CODE_DICT
    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    return unmorsed

def level_one_decrypt(enc):
	global MORSE_CODE_DICT

	s = enc.split(' ')

	unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

	o = ''
	for c in unmorsed:
		o += chr(((ord(c) - ord('A')) + 13) % 26 + ord('A'))

	return o

def level_two_decrypt(enc):
    global MORSE_CODE_DICT
    t = ''
    for c in enc:
        if c == '-':
            t += '.'
        elif c == '.':
            t += '-'
        else:
            t += ' '

    s = t.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    return unmorsed

def level_three_decrypt(enc):
    global MORSE_CODE_DICT

    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    l = len(unmorsed) // 3

    if len(unmorsed) % 3 != 0:
        l += 1

    o = ''
    cols = ['']*3

    i = 0
    idx = 0
    while i < len(unmorsed) and idx < 3:
        if idx == 0:
            cols[idx] = unmorsed[i:l]
            i += l
        elif idx == 1:
            ll = len(unmorsed[i:])
            llm = ll % 2
            cols[idx] = unmorsed[i:i+ll//2+llm]
            i += ll//2 + llm
        else:
            cols[idx] = unmorsed[i:]

        idx += 1

    for i in range(l):
        for j in range(len(cols)):
            if i < len(cols[j]):
                o += cols[j][i]

    return o

def level_four_decrypt(enc):
    global MORSE_CODE_DICT

    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    t = ''
    for c in unmorsed:
        t += chr(((ord(c) - ord('A')) + 13) % 26 + ord('A'))

    unmorsed = t

    l = len(unmorsed) // 3

    if len(unmorsed) % 3 != 0:
        l += 1

    o = ''
    cols = ['']*3

    i = 0
    idx = 0
    while i < len(unmorsed) and idx < 3:
        if idx == 0:
            cols[idx] = unmorsed[i:l]
            i += l
        elif idx == 1:
            ll = len(unmorsed[i:])
            llm = ll % 2
            cols[idx] = unmorsed[i:i+ll//2+llm]
            i += ll//2 + llm
        else:
            cols[idx] = unmorsed[i:]

        idx += 1

    for i in range(l):
        for j in range(len(cols)):
            if i < len(cols[j]):
                o += cols[j][i]

    return o

def level_five_decrypt(enc):
    global MORSE_CODE_DICT

    t = ''
    for c in enc:
        if c == '-':
            t += '.'
        elif c == '.':
            t += '-'
        else:
            t += ' '

    enc = t

    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    t = ''
    for c in unmorsed:
        t += chr(((ord(c) - ord('A')) + 13) % 26 + ord('A'))

    unmorsed = t

    l = len(unmorsed) // 3

    if len(unmorsed) % 3 != 0:
        l += 1

    o = ''
    cols = ['']*3

    i = 0
    idx = 0
    while i < len(unmorsed) and idx < 3:
        if idx == 0:
            cols[idx] = unmorsed[i:l]
            i += l
        elif idx == 1:
            ll = len(unmorsed[i:])
            llm = ll % 2
            cols[idx] = unmorsed[i:i+ll//2+llm]
            i += ll//2 + llm
        else:
            cols[idx] = unmorsed[i:]

        idx += 1

    for i in range(l):
        for j in range(len(cols)):
            if i < len(cols[j]):
                o += cols[j][i]

    return o

def level_six_decrypt(enc):
    global MORSE_CODE_DICT

    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])
    
    k = 'TUCTF'

    ki = [(26 - (ord(c) - ord('A'))) for c in k]

    o = ''
    t = unmorsed
    for i in range(len(t)):
        o += chr(((ord(t[i]) - ord('A')) + ki[i % len(ki)]) % 26 + ord('A'))

    return o

def level_seven_decrypt(enc):
    global MORSE_CODE_DICT

    t = ''
    for c in enc:
        if c == '-':
            t += '.'
        elif c == '.':
            t += '-'
        else:
            t += ' '

    enc = t

    s = enc.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    l = len(unmorsed) // 3

    if len(unmorsed) % 3 != 0:
        l += 1

    t = ''
    cols = ['']*3

    i = 0
    idx = 0
    while i < len(unmorsed) and idx < 3:
        if idx == 0:
            cols[idx] = unmorsed[i:l]
            i += l
        elif idx == 1:
            ll = len(unmorsed[i:])
            llm = ll % 2
            cols[idx] = unmorsed[i:i+ll//2+llm]
            i += ll//2 + llm
        else:
            cols[idx] = unmorsed[i:]

        idx += 1

    for i in range(l):
        for j in range(len(cols)):
            if i < len(cols[j]):
                t += cols[j][i]

    k = 'HAVEFUN'

    ki = [(26 - (ord(c) - ord('A'))) for c in k]

    o = ''
    for i in range(len(t)):
        o += chr(((ord(t[i]) - ord('A')) + ki[i % len(ki)]) % 26 + ord('A'))

    return o

try:

	# TODO Change address
	r = remote('127.0.0.1', '8888')

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_zero_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_one_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_two_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_three_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_four_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_five_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_six_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Give me text:\n')
	r.send('text\n')

	for i in range(50):
		r.recvuntil('Decrypt ')
		m = r.recvuntil('\n')[:-1]
		d = level_seven_decrypt(m)
		r.send('{}\n'.format(d))

	r.recvuntil('Here\'s your flag:\n')

	flag = r.recvuntil('}\n')[:-1]

	FLAG = 'TUCTF{CRYPT0_D03$NT_R34LLY_3V3R_3ND}'

	r.close()

	if flag == FLAG:
		sys.exit(1)

	sys.exit(0)
except Exception:
	sys.exit(0)