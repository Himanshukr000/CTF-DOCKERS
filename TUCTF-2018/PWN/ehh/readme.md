## Full  
    This is a very simple challenge  
    printf has many format string specifiers such as  
    %s, %d, %f, %c ...  
    one in particular %n doesn't print but actually writes data  
    more specifically it writes the # of bytes printed to the address specified  
    so a format string of  
	1234%n  
    would set the value of the next address on the stack to 4  
    if the address is garbage it segfaults  
	NOTE: %5$n writes the value to the 5th address on the stack (pas the format string)  
    simply there is a global variable 'val = 0xbaadaa55' and the program checks if val == 24  
    so print your string should look like this  
	0xaddr-of-val + "20 bytes of padding" + %something$n  
    this way it'll make the address at %something (i think it's 6) will be 24 and you win  
  
## TLDR  
    printf(%n) will write the # of byte printed to the next address on the stack  
    since your format string is on the stack you can arbitrarily write a single byte  
    there is a variable val that is hardcoded and then checked against a different value  
    print 24 bytes, write to val, check value, win  
