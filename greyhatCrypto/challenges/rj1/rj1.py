
# RustleJimmy 1 Block Cipher

sbox = [ ((2 * i + 1) * 0x4d / 2) & 0xFF for i in range(256) ]
sinv = sorted(range(256), key=lambda i: sbox[i])

def enc(block, key):
    block = [ord(b) for b in block]
    key = [ord(b) for b in key]

    for i in xrange(8):
        block = [ sbox[block[j] ^ key[(i + j) & 7]] for j in xrange(8) ]
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
    
    return ''.join(chr(b) for b in block)

def dec(block, key):
    block = [ord(b) for b in block]
    key = [ord(b) for b in key]

    for i in xrange(7, -1, -1):
        block = [ block[j] ^ block[i] if i != j else block[j] for j in xrange(8) ]
        block = [ sinv[block[j]] ^ key[(i + j) & 7] for j in xrange(8) ]

    return ''.join(chr(b) for b in block)
