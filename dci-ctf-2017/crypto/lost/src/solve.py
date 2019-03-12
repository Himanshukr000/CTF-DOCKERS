from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy

def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * inverse(p, n_i) * p
    return sum % prod

keys = []
data = []

for line in open('output').read().split():
    key, cipher = line.split(':')

    keys.append(int(key))
    data.append(bytes_to_long(cipher.decode('base64')))


m = crt(keys, data)

# ce que la double encryption fait est equivalente a
# (m^e mod n)^e mod n = m ^ (e*e) mod n
# on cherche donc la racine e^2 soit 3^2 = 9

print long_to_bytes(gmpy.mpz(m).root(9)[0])
