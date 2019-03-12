Challenge 5 - 60 Points
========================
Harder than strings for sure. Misleading function that you can get called RC3_NOTA_FLAG by just disassembling.

The real one is actually a global variable.

Hint
----
1. Some variables have names that carry into the executable

Solution
--------
readelf -s chal5 | grep RC3
