#!/usr/bin/python

from random import shuffle, randrange, randint
import sys
import Maze
import signal
 
moves = 'UDLR'

def signal_handler(signum, frame):
    raise Exception("Time's up!")


def next_spot(move, cur_spot):
    r = cur_spot[0]
    c = cur_spot[1]
    if move == 'U':
        r -= 1
    if move == 'D':
        r += 1
    if move == 'L':
        c -= 1
    if move == 'R':
        c += 1
    return (r, c)


def read_flag(file_name):
    with open(file_name) as filein:
        print filein.read().strip()


def run():
    sys.setrecursionlimit(10000)
    print "Stay on an optimal path."
    print "Possible moves:\nU: up\nD: down\nL: left\nR: right"
    print "You are 'P'\nThe exit is 'E'"
    print "-"*40
    print "Press enter to begin"
    raw_input()
    
    num_runs = 10
    
    for maze_num in range(num_runs):
        print(b"Maze %d" % (maze_num + 1))
        maze = Maze.maze()
        print "Number of rows:   ", maze.real_h
        print "Number of columns:", maze.real_w
        
        turn = 1
        cur_spot = maze.p
        
        maze.printmaze()
        while True:
            if maze.is_done(turn - 1, cur_spot):
                break
            print "Turn", turn, "Current row: %d Current column: %d" % cur_spot
            print "Enter your move:"
            move = raw_input().upper()
            if move not in moves or len(move) != 1:
                print "Try again"
                sys.exit(0)
            next_move = next_spot(move, cur_spot)
            if not maze.valid_step(turn, next_move):
                print "Non optimal move, your performance is subpar. Try again"
                sys.exit(0)
            cur_spot = next_move
            maze.move(cur_spot)
            turn += 1
        
        print "Congratulations! Press enter to continue."
        raw_input()
    read_flag("flag.txt")
    

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(1200)   # Twenty minutes
    try:
        run()
    except Exception, msg:
        print "Time's out!"
    
