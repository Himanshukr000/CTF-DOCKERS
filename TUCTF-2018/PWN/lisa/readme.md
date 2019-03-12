## Full  
    Probably my favorite challenge, it's got a kick to it.  
    The program asks for input thrice  
    1) This input is secure (as far as I know) and it's purpose  
	is to pose as read() arguments (more later)  
    2) This is insecure input and you have 1 byte of return addr overwrite.  
	you use this to relatively jump somwhere, but where.  
	The point of this input is to jump to the read() function in main  
	where the program gets the data from the password file.  
	But your buffer form input 1) is at the very top of the stack meaning  
	that if you send if (0, pass-addr, 40-something) then you can write to the  
	password buffer yourself and you don't need to know it  
    3) after ROPing to the read() function, write a single null byte b/c the program checks  
	by using strcmp which will yeild true because the file descriptor is 0 so you win  
	and then it cats the flag which is in Mona lisa's eyes  
  
## TLDR  
    buffer 1) setup as read arguments read(0, password-buffer-address, 43)  
    buffer 2) "A" padding + single byte to read() in main  
    buffer 3) null byte to overwrite the password buffer  
    profit boi  

