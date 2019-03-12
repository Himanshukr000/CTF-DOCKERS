# Binary 100: Gimme sum fud

This binary is vulnerable to heap buffer-overflow. You can give it some input and it will read it onto a buffer allocated on the heap. The flag is read onto another buffer allocated right after the input, so if you overflow it with the correct amount, the flag will be printed out with your input.

```
python -c "print 'B' * 143" | nc fun.ritsec.club 1338
```
