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

def keystream(key):
    assert(sorted(key) == range(54))
    deck = key[:]
    while 1:
        deck = step(deck)
        if deck[0] >= 52:
            continue
        yield deck[0] % 26

def encrypt(msg, key): #decryption and encryption are the same function
    msg = map(ord, msg)
    assert(65 <= min(msg) <= max(msg) <= 90)

    result = [(c-65+k) % 26 for c, k in zip(msg, keystream(key))]
    return ''.join(chr(x+65) for x in result)