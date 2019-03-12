import json
P = (1<<336) + 241

def group(seq, n): return [seq[i:i+n] for i in range(0, len(seq), n)]
def strToBits(s): return ''.join(map('{:08b}'.format, map(ord, s)))
def bitsToStr(bs): return ''.join(chr(int(b, 2)) for b in group(bs, 8))

def encryptBlock(message, pub):
    m = strToBits(message)
    assert(len(m) == len(pub) == 256)
    return sum(x*int(b) for x,b in zip(pub, m)) % P

def decryptBlock(cipher, pub, priv):
    U = priv
    B = [(x*U)%P for x in pub]
    t = (cipher*U)%P

    choices = set()
    for x in sorted(B, reverse=True):
        if t >= x:
            t -= x
            choices.add(x)

    bits = ''.join(('1' if (x*U)%P in choices else '0') for x in pub)
    return bitsToStr(bits)

def encrypt(message, pub):
    message += '\0' * (-len(message) % 32)
    blocks = group(message, 32)
    return [encryptBlock(block, pub) for block in blocks]

def decrypt(cipher, pub, priv):
    return ''.join(decryptBlock(block, pub, priv) for block in cipher)

# priv = json.load(open('private','r'))
# pub = json.load(open('public','r'))
# cipher = json.load(open('encrypted','r'))
# print decrypt(cipher, pub, priv)