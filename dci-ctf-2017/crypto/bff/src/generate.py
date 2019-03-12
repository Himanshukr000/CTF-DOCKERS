from Crypto.PublicKey import RSA
from secret_keys import users
from Crypto.Util.number import *
import os

e = 65537L

messages = {
    'alice': 'DCI{euler_',
    'bob': 'was_a_pretty',
    'claire': '_rad_dude}'
}


for u, m in messages.iteritems():
    key = RSA.construct((users[u], e))
    c = key.encrypt(m, 0)[0]

    with open(u + '.key', 'w') as f:
        f.write(key.exportKey())

    with open(u + '.enc', 'w') as f:
        f.write(c)

os.system("bash -c 'zip -r bff.zip {alice,bob,claire}*'")
