#!/usr/bin/python

import sys
import random
import signal

def signal_handler(signum, frame):
    raise Exception("Time's up!")


def read_flag(file_name):
    with open(file_name) as filein:
        print filein.read().strip()
        

def bin_search(number, low, high):
    mid = (low + high) / 2
    steps = 1
    answer = []
    while high - low >= 1:
        answer.append(mid)
        if number == mid:
            return answer
        elif number < mid:
            high = mid
        else:
            low = mid
        steps += 1
        mid = (low + high) / 2
    return answer


def run():
    for run in range(1, 16):
        low = 0
        high = 10 ** run
        print "Run %d\nLow: %d\nHigh: %d" % (run, low, high)
        num = random.randint(low, high)
        answer = bin_search(num, low, high)
        turn = 0
        while turn < len(answer):
            print "Input a value:"
            try:
                inp = raw_input().strip()
                inp = int(inp)
            except NumberFomatException:
                print "That is not a number, try again."
                sys.exit(0)
            if inp == num:
                print "Correct!"
                break
            elif inp < num:
                print "Higher"
            elif inp > num:
                print "Lower"
            turn += 1
        if turn == len(answer):
            print "Too many guesses!"
            sys.exit(0)
    read_flag("flag.txt")

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(600)   # 10 minutes
    try:
        run()
    except Exception, msg:
        print Exception
        print "Time's out!"
