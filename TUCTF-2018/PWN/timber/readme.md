## Full  
    most of the challenge is just for fun  
    Inputs:  
    1) Program asks for your name  
	this is where you can write X bytes up to the stack canary  
	and leak it off when it's printed  
    2) Swipe left and right  
	just for fun.  
	left does nothing  
	right has a random chance of a match  
	super swipe (s) is a gurantee  
    3) Chat  
	Here's where you actually exploit  
	NOTE: there's a function called date() that spawns  
	     a shell but is never called, intentionally  
	The expoit here is to write:  
	padding + the stack canary + moar padding + date() return address  
    There is no PIE (position independent execution) meaning the addresses don't change  
    and they can just jump anywhere without needing to leak addresses, b/c they don't change.  
  
  
## TLDR  
    Stack Canary challenge  
    1) leak the stack canary in first input  
    2) overflow return address while overwriting the stack canary  
    3) profit  

