#!/usr/bin/python

import time
import signal
import random

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
end = """
If none of the above: FAKE NUMBER

Examples:
2 => fallout
3 => survivor
4 => fallout
6 => falloutsurvivor
8 => fallout
12 => falloutsurvivor
24 => falloutsurvivor
38 => falloutradioactive
48 => falloutsurvivor
96 => falloutsurvivor
101 => FAKE NUMBER
102 => falloutsurvivorwar
202 => fallout
303 => survivor
777 => survivornucleardestruction
1613 => FAKE NUMBER
62907 => survivorshelter
"""

vals = []
for val in words.split("\n"):
    if not len(val):
        continue
    v = val.split(" - ")
    vals.append((int(v[0]), v[1]))


def read_flag(file_name):
    with open(file_name) as filein:
        print filein.read().strip()


def signal_handler(signum, frame):
    raise Exception("Time's up!")


def sol(num):
    ans = ""
    for i in vals:
        if num % i[0] == 0:
            ans += i[1]
    if not len(ans):
        return "FAKE NUMBER"
    return ans


def run():
    print "If it is divisible by x, print y"
    print "-"*40, words
    print end
    print "-"*40
    print "Press enter to begin"
    raw_input()
    num_runs = 1
    while num_runs <= 100:
        num = random.randint(1, 10 ** num_runs)
        print num
        ans = sol(num)
        inp = raw_input()
        if inp != ans:
            print "WRONG"
            return
        num_runs += 1
    read_flag("flag.txt")


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(300)   # Five minutes
    try:
        run()
    except Exception, msg:
        print "Time's out!"
