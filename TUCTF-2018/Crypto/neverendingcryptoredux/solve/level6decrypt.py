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

print level_six_decrypt(sys.argv[1])