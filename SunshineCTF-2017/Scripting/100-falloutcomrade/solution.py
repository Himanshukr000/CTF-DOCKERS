#!/usr/bin/python

import sys
import mysocket

words = """
2 - fallout
3 - survivor
5 - comrade
7 - nuclear
11 - apocalypse
13 - shelter
17 - war
19 - radioactive
23 - atom
29 - bomb
31 - radiation
37 - destruction
41 - mushroom
43 - armageddon
47 - disaster
53 - pollution
59 - military
61 - science
67 - winter
71 - death
73 - atmosphere
79 - bunker
83 - soldier
89 - danger
97 - doomsday"""
end = """If none of the above: FAKE NUMBER"""

vals = []
for val in words.split("\n"):
    if not len(val):
        continue
    v = val.split(" - ")
    vals.append((int(v[0]), v[1]))


def sol(num):
    ans = ""
    for i in vals:
        if num % i[0] == 0:
            ans += i[1]
    if not len(ans):
        return "FAKE NUMBER"
    return ans


if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print "Usage:"
        print "python %s <host> <port>" % (sys.argv[0])
        sys.exit(0)

    host = sys.argv[1]

    try:
        port = int(sys.argv[2])
    except:
        print "port must be an int"
        sys.exit(0)
    
    sock = mysocket.mysocket(host, port)
    
    line = ""
    while "enter" not in sock.recvline().lower():
        pass
    sock.sendline("")
    while True:
        line = sock.recvline()
        try:
            num = int(line)
        except:
            print line
            break
        sock.sendline(sol(num))
    
