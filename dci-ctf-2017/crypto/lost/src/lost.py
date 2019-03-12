from Crypto.PublicKey import RSA
from Crypto.Util.number import *

def generate():
    key = RSA.generate(2048, e=3)
    m = open('flag').read()

    m = key.encrypt(m, 0)[0]
    m = key.encrypt(m, 0)[0] # double encrypt for moar securitea

    return (key.publickey().n, m)


with open('output', 'w') as f:
    for i in range(6):
        k, c = generate()

        c = c.encode('base64').replace('\n', '')

        f.write(str(k) + ":" + c + "\n")
