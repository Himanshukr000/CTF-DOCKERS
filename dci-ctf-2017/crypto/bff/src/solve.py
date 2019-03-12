from Crypto.PublicKey import RSA
from Crypto.Util.number import *

e = 65537L

alice = RSA.importKey(open('alice.key').read()).n
bob = RSA.importKey(open('bob.key').read()).n
claire = RSA.importKey(open('claire.key').read()).n

alice_p = GCD(alice, bob)
alice_q = alice / alice_p

assert alice_p * alice_q == alice

bob_p = alice_p
bob_q = bob / bob_p

assert bob_p * bob_q == bob

claire_p = GCD(alice, claire)
claire_q = claire / claire_p

assert claire_p * claire_q == claire

def decrypt((p, q), enc):
    d = inverse(e, (p - 1) * (q - 1))
    c = bytes_to_long(enc)

    return long_to_bytes(pow(c, d, p * q))

out = ''

out += decrypt((alice_p, alice_q), open('alice.enc').read())
out += decrypt((bob_p, bob_q), open('bob.enc').read())
out += decrypt((claire_p, claire_q), open('claire.enc').read())

print out
