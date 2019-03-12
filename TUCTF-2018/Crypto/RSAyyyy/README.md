____________________________________________
        RSAyyyy
             
This challenge is designed to give an overview of the RSA algorithm.   
If you have a team member that is less familiar with RSA that wants to be,  
give this challenge to them.

[This](https://simple.wikipedia.org/wiki/RSA_algorithm) might be useful.



### Walkthrough:

Level 1: Calculate n

```python
n = p * q
```

Level 2: Calculate m

Convert message to hex then to an interger.
```python 
# Python 2:
m = int(message.encode('hex'), 16)

# Python 3:
m = int(binascii.hexlify(message.encode('utf-8')), 16)
```

Level 3: Calculate c

c = m^e mod n

```python 
c = pow(m, e, n)
```

Level 4: Calculating d

This one is a bit tougher.
d is the modular inverse of e mod tot(n).
So calculate tot(n) then use an implenentation of modular inverse found online:
```python
tot = (p - 1) * (q - 1)

d = modinv(e, n)
```

Level 5: Factoring n

Either use factordb or find an algorithm online.

Level 6: Breaking simple RSA

It's essentially putting together the above

1) Factor n
2) Calculate the totient
3) Calcualte d
4) Calculate m

