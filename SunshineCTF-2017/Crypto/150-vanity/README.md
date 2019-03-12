# [Crypto 150] Vanity

## Setup

So first you'll need something running python 2.7 (assuming ubuntu), then you'll want to do the following:
  - sudo pip install pybitcoin
  - sudo apt-get install socat
  - Then run this with the following

```
socat -v tcp4-l:40001,reuseaddr,fork EXEC:"python chall.py",pty,ctty,echo=0
```

The variable intensity is the difficulty, and will change how many times a team will have to fake an address.
