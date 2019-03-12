# Premium Flag Checker

Make sure you include themes/, components/, semantic.min.css, and semantic.min.js since these are part of Semantic UI, a dependency. The jquery file is modified to hide a piece of code, and is included for convenience.

In addition, this challenge has a bug; three out of four characters of the flag are leaked to the .wasm binary because of a typo. If you are reusing this problem for a future CTF, please replace the left shift in verify_flag.c:40 with a right shift. I noticed this bug halfway through the competition but didn't think it was fair to change the problem at that point.