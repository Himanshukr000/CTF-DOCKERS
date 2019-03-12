#!/usr/bin/python
from random import randint

def print_board(board, human_score, machine_score):
  print
  print "Humans: {}\tMachines: {}".format(human_score, machine_score)
  print "The board look like this: \n"

  for i in range(3):
    print " ",
    for j in range(3):
      if board[i*3+j] == 1:
        print 'X',
      elif board[i*3+j] == 0:
        print 'O',  
      elif board[i*3+j] != -1:
        print board[i*3+j]-1,
      else:
        print ' ',
      
      if j != 2:
        print " | ",
    print
    
    if i != 2:
      print "-----------------"
    else: 
      print 
      
def print_instruction():
  print "Please use the following cell numbers to make your move"
  print_board([2,3,4,5,6,7,8,9,10], 0, 0)


def get_input():
  valid = False
  while not valid:
    try:
      user = raw_input("Where would you like to place X (1-9)? ")
      user = int(user)
      if user >= 1 and user <= 9:
        return user-1
      else:
        print "That is not a valid move! Please try again.\n"
        print_instruction()
    except Exception as e:
      print user + " is not a valid move! Please try again.\n"

def get_random(board):
  while True:
    user = randint(0,8)
    if board[user] == -1:
      return user
    
def check_win(board):
  win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
  for each in win_cond:
    try:
      if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
        return board[each[0]-1]
    except:
      pass
  return -1

def play(human_score):
  board = []
  for i in range(9):
    board.append(-1)

  win = False
  move = 0
  while not win:

    # print board
    print_board(board, human_score, 0)
    print "Turn number " + str(move+1)
    if move % 2 == 0:
      turn = 'X'
    else:
      turn = 'O'

    # get user input
    if turn == 'X':
      user = get_input()
    else:
      user = get_random(board)

    while board[user] != -1:
      print "Invalid move! Cell already taken. Please try again.\n"
      user = get_input()
    board[user] = 1 if turn == 'X' else 0

    # advance move and check for end game
    move += 1
    if move > 4:
      winner = check_win(board)
      if winner != -1:
        return winner, board  
      elif move == 9:
        winner = 1
        return winner, board

def fail(board, human_score):
  print 
  print "MACHINES WIN - You'll never get the flag"
  print_board(board, human_score, 1)
  quit()

def main():
  human_score = 0
  print_instruction()
  while human_score < 500:
    result, board = play(human_score)
    if result == 1:
      human_score += 1
      print_board(board, human_score, 0)
      print
      print "HUMANS WIN!"
      print
    else:
      fail(board, human_score)

  print "Congrats!! BSIDES_CTF{eb7611da43304b5dc47f6ee607a74902}"

if __name__ == "__main__":
  main()
  

