#!/usr/bin/env python
# DOS virus emulations:
#   - TECHNO
#import whatever
from datetime import datetime, timedelta
from pygame import mixer
from subprocess import check_output
from threading import Timer
import curses
import os
import sys
import time


#global screen dimension vars
height = 0
width = 0
lastLine = -1
activated = False


def technoPayload(stdscr):
    global activated
    activated = True
    charList = ['T','E','C','H','N','O',' ',' ',' ',' ']
    currpath = os.path.abspath(os.getcwd())
    #play sound while writing to screen.
    mixer.init()
    mixer.music.load(currpath+'/techno_quieter.mp3')
    mixer.music.play(200)
    stdscr.attroff(curses.color_pair(2))
    stdscr.attron(curses.color_pair(0))
    #rest of payload
    for i in range(height-1):
        for j in range(width):
            char = charList[j % 10]
            stdscr.addch(i,j,char)
            stdscr.refresh()
            time.sleep(0.02)
        #shift list around
        charList.insert(0, charList.pop(9))
    mixer.music.stop()
    stdscr.attroff(curses.color_pair(0))
    stdscr.attron(curses.color_pair(6))
    #write final thing centered and keep on screen for a while TODO
    line1 = "                                                     " #repeats twice
    line2 = "   TTTTTTT EEEEEEE  CCCCCC H     H N     N  OOOOO    "
    line3 = "      T    E       C       H     H NN    N O     O   "
    line4 = "      T    E       C       H     H N N   N O     O   "
    line5 = "      T    EEEEE   C       HHHHHHH N  N  N O     O   "
    line6 = "      T    E       C       H     H N   N N O     O   "
    line7 = "      T    E       C       H     H N    NN O     O   "
    line8 = "      T    EEEEEEE  CCCCCC H     H N     N  OOOOO    "
    cursorx = height / 2 - 5
    cursory = (width - len(line1)) / 2
    stdscr.move(cursorx,cursory)
    stdscr.addstr(line1)
    stdscr.move(cursorx+1,cursory)
    stdscr.addstr(line2)
    stdscr.move(cursorx+2,cursory)
    stdscr.addstr(line3)
    stdscr.move(cursorx+3,cursory)
    stdscr.addstr(line4)
    stdscr.move(cursorx+4,cursory)
    stdscr.addstr(line5)
    stdscr.move(cursorx+5,cursory)
    stdscr.addstr(line6)
    stdscr.move(cursorx+6,cursory)
    stdscr.addstr(line7)
    stdscr.move(cursorx+7,cursory)
    stdscr.addstr(line8)
    stdscr.move(cursorx+8,cursory)
    stdscr.addstr(line1)
    stdscr.refresh()
    time.sleep(5)


def start(stdscr):
    global lastLine, height, width
    curses.start_color()
    stdscr.clear()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_RED,curses.COLOR_WHITE) #narrator text
    curses.init_pair(2, curses.COLOR_BLUE,curses.COLOR_WHITE) #helper text
    #village descriptor is pair 0
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_WHITE) #forest descriptor
    curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_WHITE) #ocean descriptor

    curses.init_pair(5,curses.COLOR_WHITE,curses.COLOR_CYAN) #ocean narrator
    curses.init_pair(6,curses.COLOR_BLACK,curses.COLOR_WHITE) #village narrator
    curses.init_pair(7,curses.COLOR_WHITE,curses.COLOR_GREEN) #forest narrator

    while True: #start the adventure!
        height, width = stdscr.getmaxyx()
        renderIntro(stdscr)
        curses.echo()
        choice = stdscr.getch()
        while choice != 49 and choice != 50 and choice != 51: #getch returns the decimal equivalent
            stdscr.attron(curses.color_pair(1))
            stdscr.attron(curses.A_BOLD)
            stdscr.addstr(7,0,"WRONG CHOICE.")
            stdscr.attroff(curses.color_pair(1))
            stdscr.attroff(curses.A_BOLD)
            stdscr.refresh()
            choice = stdscr.getch()
        if choice == 49:
            renderVillage(stdscr)
            time.sleep(5)
        elif choice == 50:
            renderForest(stdscr)
            time.sleep(5)
        renderOcean(stdscr)
        break;



def renderIntro(stdscr):
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(0,0,"You've no idea how you got here, or why you've washed up on the beach, but here you are, lying on the sand with the waves lapping at your feet." + (" "*(width-143)))
    stdscr.addstr(1,0,"A quick check of your surroundings will reveal three paths:"+ (" "*(width-59)))
    stdscr.attroff(curses.color_pair(1))

    stdscr.attron(curses.color_pair(6))
    stdscr.addstr(2,0,"1. A cobble-paved road that leads North through a field of golden wheat."+ (" "*(width-72)))
    stdscr.attroff(curses.color_pair(6))

    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(3,0,"2. A dirt path leading East into a heavily-wooded forest." + (" "*(width-57)))
    stdscr.attroff(curses.color_pair(3))

    stdscr.attron(curses.color_pair(4))
    stdscr.addstr(4,0,"3. A rocky path leading South along the sandy coast." + (" "*(width-52)))
    stdscr.attroff(curses.color_pair(4))

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(5,0,"Well, which path do you choose? 1, 2, or 3?" + (" "*(width-43)))
    stdscr.attroff(curses.color_pair(1))
    stdscr.move(6,0)
    stdscr.refresh()


def renderVillage(stdscr):
    global lastLine
    lastLine = 0
    stdscr.clear()
    stdscr.attron(curses.color_pair(6))
    stdscr.attron(curses.A_UNDERLINE)
    lastLine+=1
    stdscr.addstr(lastLine,0,"A voice whispers in the wind: This is not the path you're meant to be on.")
    stdscr.attroff(curses.A_UNDERLINE)
    lastLine+=1
    stdscr.addstr(lastLine,0,"You're drawn back to the sandy path....")
    stdscr.attroff(curses.color_pair(6))
    stdscr.refresh()


def renderForest(stdscr):
    global lastLine
    lastLine = 0
    stdscr.clear()
    stdscr.attron(curses.color_pair(6))
    stdscr.attron(curses.A_UNDERLINE)
    lastLine+=1
    stdscr.addstr(lastLine,0,"A voice whispers in the wind: This is not the path you're meant to be on.")
    stdscr.attroff(curses.A_UNDERLINE)
    lastLine+=1
    stdscr.addstr(lastLine,0,"You're drawn back to the sandy path....")
    stdscr.attroff(curses.color_pair(6))
    stdscr.refresh()


def renderOcean(stdscr):
    global lastLine
    global activated
    lastLine = 0
    stdscr.clear()
    stdscr.refresh()
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(lastLine,0,"At the end of a small path, winding just past a stream, is a clear pool of water. \nA small wooden hut overlooks the cove.")
    lastLine+=2
    stdscr.addstr(lastLine,0,"Within three seconds, a witch wanders out of the hut. They're not too happy to have a visitor.")
    stdscr.attroff(curses.color_pair(5))

    stdscr.attron(curses.color_pair(2))
    lastLine+=2
    stdscr.addstr(lastLine,0,"You've got exactly one minute to tell me what you want before I send you off!\n")
    stdscr.refresh()

    #the timer starts now...
    t = Timer(60,technoPayload,[stdscr])
    t.start()
    while not activated:
        stdscr.refresh()
        curses.echo()
        curses.nocbreak()
        command = raw_input("What do you want??\n")
        if "cat flag.txt" in command:
            t.cancel()
            output = check_output(['cat','flag.txt']) #what, you think we trust user input?
            lastLine+=1
            stdscr.attron(curses.A_BOLD)
            stdscr.addstr(lastLine,0,"Here's your flag: "+output)
            stdscr.attroff(curses.A_BOLD)
            stdscr.refresh()
            time.sleep(20)
            return
        else:
            continue #do nothing until we get a cat flag.txt!
    t.join()

if __name__ == '__main__':
    curses.wrapper(start) #reset terminal back to normal on error.
