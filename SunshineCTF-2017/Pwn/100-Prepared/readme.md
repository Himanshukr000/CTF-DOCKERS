# [Pwn 20] Prepared

## Setup

For setup, accurate system time is needed. This is a typical Pwnableharness setup, so just copy this folder into pwnableharness folder and run the "make docker-start" command in the base pwnableharness directory. The players will receive a copy of the binary and libpwnableharness.

## Solution

This is a simple challenge, where a random number generator uses system time as a seed. Just get the same seed, generate the same sequence, and pipe it into the program. Using the exploit binary, just type:

```bash
./exploit | nc pwn.sunshinectf.org 20001
```
