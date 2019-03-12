#!/usr/bin/python

import sys
import mysocket
import time

def readnlines(sock, n):
    for i in range(n):
        sock.recvline()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "not enough arguments"
        sys.exit(0)
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except:
        print "second argument must be an int!"
    sock = mysocket.mysocket(host, port)
    numrun = 0
    while True:
        numrun += 1
        line = sock.recvline()
        print line
        lowline = sock.recvline()
        try:
            low = int(lowline.split()[-1])
        except:
            print lowline
        highline = sock.recvline()
        try:
            high = int(highline.split()[-1])
        except:
            print highline
        line = ""
        mid = (low + high) / 2
        while True:
            line = sock.recvline().lower()
            if "correct" in line:
                print numrun, mid
                break
            
            if "flag" in line:
                print "FLAG:", line
                sys.exit(0)
            
            if "input" not in line:
                got = sock.recvline().lower()
            else:
                sock.sendline(mid)
                continue
            
            if "too many" in got:
                sys.exit(0)
                
            if "lower" in line:
                high = mid
            elif "higher" in line:
                low = mid
            elif "too many" in line:
                sys.exit(0)
            elif "correct" in line:
                break
            mid = (low + high) / 2
            sock.sendline(mid)
    sock.close()
