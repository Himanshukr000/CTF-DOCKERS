import os
import hashlib
import struct

class SlippyCipher(object):

    def __init__(self, key):
        pass

    def weak_block_encrypt(self, block, subkey):
        """
        This is a pretty terrible block cipher. Thankfully, we can make it
        much stronger through iteration.
        """

        # N.B. 2xy+x+y is an invertible operation over numbers mod a power of 2
        x = (2 * block * subkey + block + subkey) % 2**64

        # left rotate by 1
        x = ((x << 1) | (x >> 63)) % 2**64

        # just some salt
        x = x ^ 0x3CAB470ADB580357

        return x

    def weak_block_decrypt(self, block, subkey):
        pass

    def strong_block_encrypt(self, block, key):
        """
        If I had an iteration of this cipher for every fluid ounce of coke
        in a vending machine bottle of coke, this construction would be 
        obviously secure.
        """

        for i in xrange(4096):
            block = self.weak_block_encrypt(block, key)

        return block

    def encrypt(self, message):        
        """
        Encrypt using CBC mode with the generated table as the block cipher.
        """

        # convert any Unicode characters to UTF-8
        message = message.encode('utf-8')

        # pad to multiple of block size
        message += chr(8 - len(message) % 8) * (8 - len(message) % 8)

        # cut message into words as 16-bit numbers
        message = [struct.unpack('<Q', message[i:i+8])[0]
                   for i in xrange(0, len(message), 8)]

        ciphertext = []

        # generate IV
        iv = struct.unpack('<H', os.urandom(2))[0]
        ciphertext.append(iv)

        # encrypt using CBC mode
        last = iv
        for mblk in message:
            cblk = self._table[mblk ^ last]
            ciphertext.append(cblk)
            last = cblk

        return ''.join(struct.pack('<H', w) for w in ciphertext)

    def decrypt(self, ciphertext):
        pass
