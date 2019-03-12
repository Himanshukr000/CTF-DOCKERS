#!/usr/bin/env python2


import sys

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

print level_seven_decrypt(sys.argv[1])