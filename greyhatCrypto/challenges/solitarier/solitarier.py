def step(deck):
    i = deck.index(52)
    deck.remove(52)
    i -= 1
    if i <= 0:
        i -= 1
    deck.insert(i % 54, 52)

    i = deck.index(53)
    deck.remove(53)
    i -= 2
    if i <= 0:
        i -= 1
    deck.insert(i % 54, 53)

    i = deck.index(52)
    j = deck.index(53)
    a, b = sorted((i, j))
    b += 1
    deck = deck[b:] + deck[a:b] + deck[:a]

    #maybe another step to make things more secure? TODO
    return deck

POPCOUNT = 13
def keystream(key):
    assert(sorted(key) == range(54))
    deck = key[:]
    while 1:
        deck = step(deck)
        if max(deck[:POPCOUNT]) == 52:
            continue
        yield sum(deck[:POPCOUNT]) % 29

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ {}'
def encrypt(msg, key): #decryption and encryption are the same function
    msg = map(chars.index, msg)
    result = [(c+k) % 29 for c, k in zip(msg, keystream(key))]
    return ''.join(chars[x] for x in result)

# import random
# key = range(54)
# random.SystemRandom().shuffle(key)
# msg = open('message.txt', 'r').read()
# cipher = encrypt(msg, key)
# open('encrypted.txt', 'w').write(cipher)