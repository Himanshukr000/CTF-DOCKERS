cipher = open('cipher_text', 'r').read()
cipher = cipher.strip()
cipher = [int(num) for num in cipher.split()]
print cipher
i = 0
res = ''
while i < len(cipher):
    print i
    possible = []
    possible = [(x, chr(sum(cipher[i:i+x])^61)) for x in range(2, 6) if i+x <= len(cipher) and sum(cipher[i:i+x])^61 >= 0xa and sum(cipher[i:i+x])^61 < 0x7e and not chr(sum(cipher[i:i+x])^61).islower()]
    if len(possible) ==1 and possible[0][1] == '\n':
        break
    print ("Possibilities :", [p[1] for p in possible])
    user_input = raw_input("Guess? ")
    i += [p[0] for p in possible if user_input.upper() == p[1]][0]
    res += user_input.lower()
print res
