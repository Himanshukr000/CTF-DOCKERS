## Full  
    fun little challenge  
    They are given a .pyc file (a compiled python file)  
    They must first decompile it, I recommend uncompyle6  
    The code prints out a funny, but familiar, looking string  
    Inside the decompiled code there are 4 functions  
    They must execute the functions on the string in this order  
	reverse  
	base32decode  
	rot13  
	reversePigLatin  
    Then it's the plaintext flag  
  
## TLDR  
    Decompile .pyc with uncompyle6  
    Figure out which order to run the functions in the code on the  
    funny looking string to get the flag  

