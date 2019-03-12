## Full  
    Easist shellcode challenge yo mama eva' saw!  
    DEP, which prevents you from exeucting code on the stack, is disabled  
    and you have 64 bytes of shellcode to write, which is more than plenty  
    I leak the address on the stack so there's no problem there.  
    There is 1 twist though  
    There's a value on the stack 0xcafebabe and checks later if it's 0xdeadbeef  
    this way there's 1 cave-ot to this program. You gotta change that value  
    just to get people to look at some addresses or something I dunno  
    Then syscall your way to victory with some good shellcode  
  
## TLDR  
    no DEP ie. you can execute on the stack  
    although there is a value on the stack that needs to be 0xdeadbeef  
    so you can't just carelessly overwrite. You gotta make that value right  
    Other than that, I leak stack addr, you write shellcode, you win  

