#!/usr/bin/env python2

import sys, string

from pwn import *


try:
	# TODO Change address
	r = remote('127.0.0.1', 8888)

	chars = string.printable

	flag = ''

	for i in range(32):
		r.recvuntil('Enter your text here: ')

		amt = 32 - i - 1
		pad = '_'*amt
		padc = '_'*(amt-i)

		r.send('{}\n'.format(pad))
		r.recvuntil('Here\'s your encrypted text:\n')

		h = r.recvline()[:64]

		for c in chars:
			s = pad + flag + c
			# print s

			r.recvuntil('Enter your text here: ')
			r.send('{}\n'.format(s))

			r.recvuntil('Here\'s your encrypted text:\n')

			hc = r.recvline()[:64]

			if hc == h:
				flag += c
				break

	r.close()

	FLAG = 'TUCTF{A3S_3CB_1S_VULN3R4BL3!!!!}'

	if flag == FLAG:
		print 'guchi'
		sys.exit(1)

	sys.exit(0)

except Exception:
	sys.exit(0)