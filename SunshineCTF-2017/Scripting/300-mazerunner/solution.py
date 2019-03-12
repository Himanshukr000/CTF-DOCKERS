#!/usr/bin/python
import sys
import socket
import Queue
import time

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


def sendline(sock, string):
    sock.send("".join([string, '\n']))


def readline(sock):
    s = ""
    c = sock.recv(1)
    while c != '\n':
        s = "".join([s, c])
        c = sock.recv(1)
    return s


def readnlines(sock, n, print_it=None):
    for i in range(n):
        v = readline(sock)
        if print_it:
            print v


def solve(maze):
    grid = []
    start, end = None, None
    r = 0
    for i in maze:
        c = 0
        cur = []
        for j in i:
            if j == 'P':
                start = (r, c)
                cur.append(0)
            elif j == 'E':
                end = (r, c)
                cur.append(-1)
            elif j == ' ' or j == 'E':
                cur.append(-1)
            else:
                cur.append(1000000)
            c += 1
        r += 1
        grid.append(cur)
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    cur = start
    q = Queue.Queue()
    q.put(cur)
    
    while not q.empty():
        cur = q.get()
        for i in range(4):
            n = (cur[0] + dr[i], cur[1] + dc[i])
            if (n[0] < 0 or n[0] >= len(grid) or n[1] < 0 \
                                or n[1] >= len(grid[0])):
                continue
            if grid[n[0]][n[1]] < 0:
                grid[n[0]][n[1]] = grid[cur[0]][cur[1]] + 1
                q.put(n)
    r = 0
    for i in grid:
        c = 0
        for j in i:
            if j == 1000000:
                grid[r][c] = -1
            c += 1
        r += 1
    
    path = ""
    cur = end
    poss = ['D', 'L', 'U', 'R']
    while cur != start:
        for i in range(4):
            cr = cur[0] + dr[i]
            cc = cur[1] + dc[i]
            if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[0]):
                continue
            if grid[cr][cc] - grid[cur[0]][cur[1]] == -1:
                cur = (cr, cc)
                path = "".join([poss[i], path])
                break
    return path


if __name__ == "__main__":
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    readnlines(sock, 10, True)
    while True:
        sendline(sock, "")
        line = readline(sock)
        print line
        if "flag" in line:
            break
            
        rows_line = readline(sock)
        cols_line = readline(sock)
        print "num rows:", rows_line
        print "num cols:", cols_line
        num_rows = int(rows_line.split()[-1])
        num_cols = int(cols_line.split()[-1])
        
        grid = [readline(sock) for i in range(num_rows)]
        path = solve(grid)
        readline(sock)
        readline(sock)
        sendline(sock, path[0])
        for i in range(1, len(path)):
            readnlines(sock, 2)
            sendline(sock, path[i])
        readline(sock)
    
    
