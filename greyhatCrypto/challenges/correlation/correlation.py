class LCG(object):
    def __init__(self, a, c, x):
        self.a = a
        self.c = c
        self.x = x
        self.mod = 1<<32

    def next(self):
        self.x *= self.a
        self.x += self.c
        self.x %= self.mod
        return self.x >> 31

def keystream(k):
    g1 = LCG(71664525, 1013904223, int(k[:3], 16))
    g2 = LCG(22695477, 1010101011, int(k[3:6], 16))
    g3 = LCG(11015245,  987654321, int(k[6:9], 16))
    gens = g1, g2, g3

    for _ in range(20):
        for g in gens:
            g.next()

    while 1:
        b = 0
        for i in range(8):
            bits = [g.next() for g in gens]
            val = sum(bits) // 2
            b |= val << i
        yield b

def encrypt(data, key='000000000'):
    return ''.join(chr(ord(x) ^ y) for x,y in zip(data, keystream(key)))