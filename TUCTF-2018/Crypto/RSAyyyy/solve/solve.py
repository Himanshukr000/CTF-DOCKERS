#!/usr/bin/env python2

import sys

from pwn import *

def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x

def factor(N):
    if N%2==0:
        return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:             
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                    y = ((y*y)%N+c)%N
                    q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break
 
    return g

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

try:
	# TODO Change address
	r = remote('3.16.57.250', '12345')

	r.recvuntil('p = ')

	m = r.recvuntil('\n')[:-1]

	p = int(m)

	r.recvuntil('q = ')

	m = r.recvuntil('\n')[:-1]

	q = int(m)

	n = p * q

	r.recvuntil('What is n?\n')

	r.send('{}\n'.format(n))

	r.recvuntil('message = "')

	m = r.recvuntil('"')[:-1]

	msg = int(m.encode('hex'), 16)

	r.send('{}\n'.format(msg))

	r.recvuntil('p = ')

	m = r.recvuntil('\n')[:-1]

	p = int(m)

	r.recvuntil('q = ')

	m = r.recvuntil('\n')[:-1]

	q = int(m)

	n = p * q

	r.send('{}\n'.format(n))

	r.recvuntil('e = ')

	m = r.recvuntil('\n')[:-1]

	e = int(m)

	r.recvuntil('m = ')

	m = r.recvuntil('\n')[:-1]

	msg = int(m)

	c = pow(msg, e, n)

	r.recvuntil('What is c?\n')

	r.send('{}\n'.format(c))

	r.recvuntil('p = ')

	m = r.recvuntil('\n')[:-1]

	p = int(m)

	r.recvuntil('q = ')

	m = r.recvuntil('\n')[:-1]

	q = int(m)

	tot = (p - 1) * (q - 1)

	r.recvuntil('What is tot(n)?\n')

	r.send('{}\n'.format(tot))

	r.recvuntil('e = ')

	m = r.recvuntil('\n')[:-1]

	e = int(m)

	d = modinv(e, tot)

	r.recvuntil('What is d?\n')

	r.send('{}\n'.format(d))

	r.recvuntil('n = ')

	m = r.recvuntil('\n')[:-1]

	n = int(m)

	p = factor(n)

	q = n / p

	r.recvuntil('What is p?\n')

	r.send('{}\n'.format(p))

	r.recvuntil('What is q?\n')

	r.send('{}\n'.format(q))

	r.recvuntil('c = ')

	m = r.recvuntil('\n')[:-1]

	c = int(m)

	r.recvuntil('n = ')

	m = r.recvuntil('\n')[:-1]

	n = int(m)

	r.recvuntil('e = ')

	m = r.recvuntil('\n')[:-1]

	e = int(m)

	r.recvuntil('What is p?\n')

	p = factor(n)

	q = n / p

	r.send('{}\n'.format(p))

	r.recvuntil('What is q?\n')

	r.send('{}\n'.format(q))

	r.recvuntil('What is tot(n)?\n')

	tot = (p - 1) * (q - 1)

	r.send('{}\n'.format(tot))

	r.recvuntil('What is d?\n')

	d = modinv(e, tot)

	r.send('{}\n'.format(d))

	r.recvuntil('Finally, what is m?\n')

	m = pow(c, d, n)

	r.send('{}\n'.format(m))

	r.recvuntil('Here\'s your flag:\n')

	flag = r.recvuntil('}\n')[:-1]

	FLAG = 'TUCTF{RSA_1$_R34LLY_C00L_4ND_1MP0RT4NT_CRYPT0}'

	r.close()

	if flag == FLAG:
        print 'guchi'
		sys.exit(1)

	sys.exit(0)
except Exception:
	sys.exit(0)
