# Forensics Question 1

For this question we were given a password protected zip [file](clue.zip) and the following brainfuck code
```
->-.>-.---.-->-.>.>+.-->--..++++.
.+++.
.->-.->-.++++++++++.+>+++.++.-[->+++<]>+.+++++.++++++++++..++++[->+++<]>.--.->--.>.
```
I first tried to use fcrackzip to crack the password of the zip file with no luck. So I printed the brainfuck code output and thought I could use it for a partial plaintext attack using pcrackzip.
After failing with those programs I had the thought to use John. I found that [bleeding-jumbo](https://github.com/magnumripper/JohnTheRipper) came with a zip2john program that extracted a zip password hash from an encrypted zip file.
After extracting the hash I ran john with the hash and the zip file and got the password in about a second. The password was: dissect. After cracking the zip file I ran strings on clue.pcap and got the flag

pragyanctf{5n00p_d099}
