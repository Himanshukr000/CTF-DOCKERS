# ActuallySolveable Block Cipher

def bytesToInt(xs): return sum(x<<(i*8) for i,x in enumerate(xs))
def intToBytes(x): return [(x >> (8 * i)) & 0xFF for i in xrange(8)]

sbox = [ ((2 * i + 0x101) * 0x61 / 2) & 0xFF for i in range(256) ]
sinv = sorted(range(256), key=lambda i: sbox[i])

def T(block):
    # bit transpose of 8 bytes
    x = bytesToInt(block)
    t = (x ^ (x >> 7)) & 0x00AA00AA00AA00AAL
    x = x ^ t ^ (t << 7)
    t = (x ^ (x >> 14)) & 0x0000CCCC0000CCCCL
    x = x ^ t ^ (t << 14)
    t = (x ^ (x >> 28)) & 0x00000000F0F0F0F0L
    x = x ^ t ^ (t << 28)
    return intToBytes(x)

def R(byte, n):
    return (byte >> n) | ((byte & ((1 << n) - 1)) << (8 - n))

def encrypt_round(block, key):
    for i in xrange(8):
    # for i in xrange(3):
        block = [ block[j] ^ key[(i + j) & 0x7] for j in xrange(8) ]
        block = [ sbox[block[j]] for j in xrange(8) ]
        block = [ R(block[j], j) for j in xrange(8) ]
        block = T(block)
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
    return [ block[j] ^ key[j] for j in xrange(8) ]

def decrypt_round(block, key):
    block = [ block[j] ^ key[j] for j in xrange(8) ]
    for i in xrange(7, -1, -1):
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
        block = T(block)
        block = [ R(block[j], 8 - j) for j in xrange(8) ]
        block = [ sinv[block[j]] for j in xrange(8) ]
        block = [ block[j] ^ key[(i + j) & 0x7] for j in xrange(8) ]
    return block

def encrypt(message, key):
    message += [0] * (-len(message) % 8)
    out = []
    iv = [0]*8
    for bi in range(len(message)//8):
        block = message[bi*8:bi*8+8]
        block = [x^y for x,y in zip(block, iv)]
        block2 = encrypt_round(block, key)
        out += block2
        iv = block2
    return out

def decrypt(message, key):
    out = []
    iv = [0]*8
    for bi in range(len(message)//8):
        block = message[bi*8:bi*8+8]
        block2 = decrypt_round(block, key)
        block2 = [x^y for x,y in zip(block2, iv)]
        out += block2
        iv = block
    return out