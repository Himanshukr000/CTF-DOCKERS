## Full  
    This is one hell of a challenge --> shella hard  
    So this challenge is as simple as it gets  
    the main function just reads and nothing else and you can clearly overwrite the return address  
    there is one other function named giveShell()  
    Now this program simply spawns a shell using execve("/bin/sh", 0, 0) which spawns a shell  
    The trick to all of this I added 3 NOPs before the execve and changed the last two to  
    a1 44 which takes the program from  
	nop  
	nop  
	nop  
	push 0  
	push 0  
	push 0x... -> "/bin/sh"  
	execve  
    to  
	nop  
	mov ...  
	add ...  
	push ..  
	push ..  
	push ..  
	call execve  
    now with this code, it's broken and doesn't execute at all b/c  
    the first mov is a bad address  
    This goal of this challenge is to jump to the first 'push 0' and you'll get a shell  
    but you can't normally see that  
  
  
## TLDR  
    Clear return address overwrite  
    giveShell function that spawns a shell  
    BUT  
    giveShell has 2 messed up bits that hide most of the function and causes  
    it to break when executed  
    Jump after these 2 bytes and Bob's your uncle  

