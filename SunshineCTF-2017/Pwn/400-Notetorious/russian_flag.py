#!/usr/bin/env python

BG_WHITE = "\033[107m"
BG_BLUE = "\033[44m"
BG_RED = "\033[41m"
RESET = "\033[m"

spaces = " "*36
white_row = BG_WHITE + spaces + RESET
blue_row = BG_BLUE + spaces + RESET
red_row = BG_RED + spaces + RESET

for row in (white_row, blue_row, red_row):
	for rownum in range(4):
		print(row)
