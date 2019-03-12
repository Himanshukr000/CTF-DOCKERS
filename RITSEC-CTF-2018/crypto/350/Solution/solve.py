#!/usr/bin/python

from Crypto.Cipher import AES
import binascii
import string
import itertools

# given
bKEY = "9aF738g9AkI112"

# use null bytes to minimize effect on output
IV = "\x00"*16


def encrypt(message, passphrase):
   aes = AES.new(passphrase, AES.MODE_CBC, IV)
   return aes.encrypt(message)

def decrypt(cipher, passphrase):
   aes = AES.new(passphrase, AES.MODE_CBC, IV)
   return aes.decrypt(cipher)


pt = "The message is protected by AES!"
#ct = "b00000000000000000000000000024bd3df9b0396cd7181bf60e554493fd5888"
ct = "2a0000000000000000000000000015f8fecfcfefd7a042d0921201af50d1ef57"

# find the key using the plaintext and ciphertext we know, since the IV has no effect on the decryption of the second block
for i in itertools.product(string.printable, repeat=2):
   eKEY = ''.join(i)
   KEY = bKEY + eKEY
   ptc = decrypt(binascii.unhexlify(ct), KEY)
   if ptc[16] == pt[16] and ptc[30] == pt[30] and ptc[31] == pt[31]:
       print "Got KEY: " + str(KEY)
       fKEY = KEY
       pt2 = binascii.hexlify(decrypt(binascii.unhexlify(ct), fKEY))[32:]
       print "Decrypting with CT mostly zeroes gives: " + pt2
       print "Should be: " + binascii.hexlify(pt[16:])
# we can now recover the rest of the ciphertext ct by XOR(pt[i], decrypted[i], since we chose ct 00 in all the positions we are going to recover
       answer = ""
       for i in range(13):
           pi = pt[17+i]  # letters from the plaintext
           pti = pt2[2*i+2:2*i+4]  # 2 hex letters from decryption of second block
           answer += "%02X" % (ord(pi) ^ int(pti, 16))
       rct = ct[0:2] + answer.lower() + ct[28:]
       print "Which means CT was: " + rct

# now we can decrypt the recovered ct and xor against the pt to recover the IV
wpt = decrypt(binascii.unhexlify(rct), fKEY)
IV = ""
for i in range(16):
   p = ord(pt[i]) ^ ord(wpt[i])
   IV += "%02X" % p
IV = binascii.unhexlify(IV)

# sanity check:
aes = AES.new(fKEY, AES.MODE_CBC, IV)
print "Sanity check: " + aes.decrypt(binascii.unhexlify(rct))

# We won!
print "The IV is: " + IV
