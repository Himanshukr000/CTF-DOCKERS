import string
import random


def alpha(w):
    return [w[1], w[0]]


def beta(w):
    w[0][0] ^= w[1][3]
    w[0][1] ^= w[1][2]
    w[0][2] ^= w[1][1]
    w[0][3] ^= w[1][0]
    return w


def gamma(w):
    return [[w[1][3], w[1][0], w[1][2], w[0][0]],
            [w[1][1], w[0][3], w[0][1], w[0][2]]]


def rotl(num, bits=8):
    bit = num & (1 << (bits - 1))
    num <<= 1
    if (bit):
        num |= 1
    num &= (2**bits - 1)

    return num


def rotr(num, bits=8):
    num &= (2**bits - 1)
    bit = num & 1
    num >>= 1
    if (bit):
        num |= (1 << (bits - 1))

    return num


def delta(w):
    w[0][0] = rotl(w[0][0])
    w[1][0] = rotl(w[1][0])
    w[0][2] = rotl(w[0][2])
    w[1][2] = rotl(w[1][2])

    w[0][1] = rotr(w[0][1])
    w[1][1] = rotr(w[1][1])
    w[0][3] = rotr(w[0][3])
    w[1][3] = rotr(w[1][3])
    return w


def do_round(w):
    return delta(gamma(beta(alpha(w))))


def to_matrix(w):
    return [[w[0], w[1], w[2], w[3]], [w[4], w[5], w[6], w[7]]]


def from_matrix(w):
    return [
        w[0][0], w[0][1], w[0][2], w[0][3], w[1][0], w[1][1], w[1][2], w[1][3]
    ]


def f(w):
    w = to_matrix(w)
    for i in range(50):
        w = do_round(w)
    return from_matrix(w)


def hash_func(string):
    S = [31, 56, 156, 167, 38, 240, 174, 248]
    while string != "":
        letters = 1
        s = [ord(string[0])]
        if len(string) > 1:
            s.append(ord(string[1]))
            letters = 2
        if len(string) > 2:
            s.append(ord(string[2]))
            letters = 3
        if len(string) > 3:
            s.append(ord(string[3]))
            letters = 4
        string = string[letters:]
        for i in range(len(s)):
            S[i] ^= s[i]
        S = f(S)
    return S[:4]


def main():
    n = 10
    i = 0
    seen = {}
    while True:
        plain = ''.join(
            random.choices(
                string.ascii_uppercase + string.ascii_lowercase, k=n))
        hash1 = hash_func(plain)
        if i % 1000 == 0:
            print("At attempt number {}".format(i))
        if str(hash1) in seen and seen[str(hash1)] != plain:
            print("Found it {} and {} in {} tries with hash 0x{}.".format(
                plain, seen[str(hash1)], i,
                ''.join('{:02x}'.format(x) for x in hash1)))
            break
        seen[str(hash1)] = plain
        i += 1


def other_main():
    strin1 = input("Input String 1: ")
    strin2 = input("Input String 2: ")
    hash1 = hash_func(strin1)
    hash2 = hash_func(strin2)
    print("The hashes for '{}' and '{}' hash to 0x{} and 0x{}.".format(
        strin1, strin2, ''.join('{:02x}'.format(x) for x in hash1),
        ''.join('{:02x}'.format(x) for x in hash2)))


if __name__ == '__main__':
    #other_main()
    main()
