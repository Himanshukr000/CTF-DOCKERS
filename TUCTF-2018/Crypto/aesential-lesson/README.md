_____________________________________
        AESential Lesson
        
Thought I'd give you an essential lesson to
how you shouldn't get input for AES in ECB mode.

nc {need address} {need port}



### Walkthrough

Send 'X'*31 to server. That will return an encryption of 
'X'*31 + first char of flag. Now send in a loop, 'X'*31 + guess char,
then compare each guess's encryption with the previous result.

Now you have one character, so send 'X'*30 + known char. This will give second
character. Now guess with 'X'*31 + known char + guess char. Repeat this until
have flag.