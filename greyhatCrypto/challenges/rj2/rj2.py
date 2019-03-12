
# RustleJimmy 2 Block Cipher

sbox = [ ((2 * i + 1) * 0x4d / 2) & 0xFF for i in range(256) ]
sinv = sorted(range(256), key=lambda i: sbox[i])

def T(block):
    # bit transpose of 8 bytes
    x = sum(block[i] << (8 * i) for i in xrange(8))
    t = (x ^ (x >> 7)) & 0x00AA00AA00AA00AAL
    x = x ^ t ^ (t << 7)
    t = (x ^ (x >> 14)) & 0x0000CCCC0000CCCCL
    x = x ^ t ^ (t << 14)
    t = (x ^ (x >> 28)) & 0x00000000F0F0F0F0L
    x = x ^ t ^ (t << 28)
    return [ (x >> (8 * i)) & 0xFF for i in xrange(8) ]

def R(byte, n):
    return (byte >> n) | ((byte & ((1 << n) - 1)) << (8 - n))

def enc(block, key):
    block = [ord(b) for b in block]
    key = [ord(b) for b in key]

    for i in xrange(8):
        block = [ block[j] ^ key[(i + j) & 0x7] for j in xrange(8) ]
        block = [ sbox[block[j]] for j in xrange(8) ]
        block = [ R(block[j], j) for j in xrange(8) ]
        block = T(block)
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
    block = [ block[j] ^ key[j] for j in xrange(8) ]

    return ''.join(chr(b) for b in block)

def dec(block, key):
    block = [ord(b) for b in block]
    key = [ord(b) for b in key]

    block = [ block[j] ^ key[j] for j in xrange(8) ]
    for i in xrange(7, -1, -1):
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
        block = T(block)
        block = [ R(block[j], 8 - j) for j in xrange(8) ]
        block = [ sinv[block[j]] for j in xrange(8) ]
        block = [ block[j] ^ key[(i + j) & 0x7] for j in xrange(8) ]

    return ''.join(chr(b) for b in block)
