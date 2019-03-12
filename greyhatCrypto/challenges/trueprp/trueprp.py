import os
import hashlib
import struct

class TruePRP(object):

    @classmethod
    def _key_rand(cls, key, i):
        """
        Generate a random number deterministically from the key in the range
        0 <= n <= i. Outputs for independent i are not correlated in any way.
        """

        return struct.unpack('<Q', hashlib.sha512('%d:%s'% (i, key)).digest()[:8])[0] % i

    def __init__(self, key):
        """
        Generate a permutation table for every input 16-bit word.
        
        This permutation is randomly sampled from all 16-bit permutations,
        so it is a *true* random permutation: there can be no weaknesses! 
        There are log2(16!) = 2^45 such permutations, so 45 bits of key
        entropy should be sufficient.

        Note that this table applies to LITTLE ENDIAN 16-bit words.
        """
        
        self._table = [ i for i in xrange(2**16) ]
        self._inv_table = [ 0 for i in xrange(2**16) ]

        # generate table using Fisher-Yates shuffle
        for i in xrange(2**16-1, 0, -1):
            j = TruePRP._key_rand(key, i)
            self._table[i], self._table[j] = self._table[j], self._table[i]

        # generate inverse table
        for i in xrange(2**16):
            self._inv_table[self._table[i]] = i

    def encrypt(self, message):
        """
        Encrypt using CBC mode with the generated table as the block cipher.
        """

        # pad to multiple of block size
        if len(message) % 2 == 0:
            message += '\x02\x02'
        else:
            message += '\x01'

        # cut message into words as 16-bit numbers
        message = [struct.unpack('<H', message[i:i+2])[0]
                   for i in xrange(0, len(message), 2)]

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
        """
        Decrypt using CBC mode with the generated inverse table as the inverse block cipher
        """
        
        # cut ciphertext into blocks as 16-bit numbers
        ciphertext = [struct.unpack('<H', ciphertext[i:i+2])[0] 
                      for i in xrange(0, len(ciphertext), 2)]

        message = []

        # decrypt using CBC mode
        for i in xrange(1, len(ciphertext)):
            cblk = ciphertext[i]
            last = ciphertext[i-1]
            mblk = self._inv_table[cblk] ^ last
            message.append(mblk)

        message = ''.join(struct.pack('<H', w) for w in message)

        # remove padding
        if message[-1] == '\x01':
            message = message[:-1]
        else:
            message = message[:-2]

        return message
