#!/usr/bin/python

from random import shuffle, randrange, randint
import sys
import Queue

def printerr(string):
    sys.stderr.write("".join([string, "\n"]))

class maze(object):
    
    def __init__(self, h=None, w=None):
        if w is None:
            self.w = randint(10, 20)
        else:
            self.w = w
        if h is None:
            self.h = randint(10, 20)
        else:
            self.h = h
        
        self.real_h = self.h * 2 + 1
        self.real_w = self.w * 2 + 1
        self.maze = self.make_maze()
        self.p = self.randspot()
        self.e = self.randspot()
        
        while self.man_dist(self.p, self.e) < min([self.w, self.h, 40]):
            self.e = self.randspot()
        
        maze = self.maze
        p = self.p
        e = self.e
        maze[p[0]][p[1]] = 'P'
        maze[e[0]][e[1]] = 'E'
        
        self.shortest = 0
        self.grid, self.shortest = self.solve()
    
    def make_maze(self):
        """
        Maze generation algorithm taken from:
        https://rosettacode.org/wiki/Maze_generation#Python
        """
        w = self.w
        h = self.h
        
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+-"] * w + ['+'] for _ in range(h + 1)]
     
        def walk(x, y):
            vis[y][x] = 1
     
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+ "
                if yy == y: ver[y][max(x, xx)] = "  "
                walk(xx, yy)
     
        walk(randrange(w), randrange(h))
     
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return [list(i) for i in s.strip().split('\n')]
    
    def solve(self):
        grid = []
        r = 0
        for i in self.maze:
            c = 0
            cur = []
            for j in i:
                if j == 'P':
                    cur.append(0)
                elif j == ' ' or j == 'E':
                    cur.append(-1)
                else:
                    cur.append(1000000)
                c += 1
            r += 1
            grid.append(cur)
        
        start = self.p
        end = self.e
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        cur = start
        q = Queue.Queue()
        q.put(cur)
        
        while not q.empty():
            cur = q.get()
            for i in range(4):
                n = (cur[0] + dr[i], cur[1] + dc[i])
                if (n[0] < 0 or n[0] >= len(grid) or n[1] < 0
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
        shortest = grid[self.e[0]][self.e[1]]
        return grid, shortest
    
    def valid_step(self, step_num, loc):
        return self.grid[loc[0]][loc[1]] == step_num
    
    def is_done(self, step_num, loc):
        return self.grid[loc[0]][loc[1]] == step_num == self.shortest
    
    def randspot(self):
        h = len(self.maze)
        w = len(self.maze[0])
        num_spots = h * w
        while True:
            rand_spot = randint(1, num_spots) - 1
            spot = (rand_spot / w, rand_spot % w)
            if self.maze[spot[0]][spot[1]] == ' ':
                return spot
    
    def move(self, next_spot):
        if self.man_dist(next_spot, self.p) == 1:
            p = self.p
            self.maze[p[0]][p[1]] = ' '
            self.maze[next_spot[0]][next_spot[1]] = 'P'
            self.p = next_spot
    
    def printmaze(self):
        print "\n".join([''.join([i for i in j]) for j in self.maze])
    
    def print_grid(self):
        longest = len(str(self.max_furthest())) + 1
        for i in self.grid:
            print " ".join([("%" + str(longest) + "d") % j for j in i])
    
    def getmaze(self):
        return "\n".join(self.maze)
    
    def man_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def max_furthest(self):
        return max([max(i) for i in self.grid])

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    m = maze(10, 10)
    m.printmaze()
    print "-"*40
    print "Input value:"
    value = raw_input()
    print "value:", value
    print "-"*30
    
    
