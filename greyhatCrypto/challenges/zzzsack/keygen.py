import random, json

P = 0x200000000000000000000000000000000000000000000000000000000000000004d

def genKey(rand=random.SystemRandom()):
    W = rand.randint(P//32, 31*P//32)
    base = []
    tot = 0

    for _ in range(256):
        x = tot + 1 + rand.getrandbits(8)
        base.append(x)
        tot += x
    assert(tot < P)

    public = [(x * W) % P for x in base]
    rand.shuffle(public)

    private = pow(W, P-2, P)
    return private, public

if __name__ == "__main__":
    priv, pub = genKey()
    json.dump(priv, open('private','w'))
    json.dump(pub, open('public','w'))