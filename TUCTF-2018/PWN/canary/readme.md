## Full  
    So for this challenge I wrote my own stack canary implementation  
    and it's vulnerable in a different way  
    So this program only gets input once.  
    Here's how my stack canary data structure is laid out:  
	-String data (40 bytes)  
	-stack canary value  
	-array index  
    So the String data is just the data  
    The Stack canary value is the value you don't know (randomly gen'd)  
    And the array index is the main part of this.  
    I wanted to make the data structure dynamic so You didn't have to remember  
    where the value was stored and just read/write data. SO, the canary DS stores  
    the index where the randomly gen'd value is stored in a global array in .data  
    This way checkCanary() just needs the canary and it'll check it for you.  
    This is important because the array that stores all the canary values is blank. Just 0's  
    So if you change the index of the first canary made (the only canary made) from 0 to 1  
    and just write 0's to the canary value then you pass the check.  
    So here's what you write  
    40bytes padding + 0 (4bytes) + 1 (4 bytes) + padding + return address  
    There is no PIE so you don't need to leak a code address, just jump to system()  
  
## TLDR  
    I made my own stack canary that holds 3 values  
	your data  
	canary value  
	index to global array  
    the array has all 0's so if you overwrite your canary value to 0's and the   
    index to 1 (where no canary has been created) You'll pass the check and can overwrite  
    the return address  
