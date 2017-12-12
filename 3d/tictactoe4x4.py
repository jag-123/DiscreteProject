import random
from minimax import AI
import math

from settings import *

class TicTacToe3D():
    new_combos = winning_combos[:]

    for i,combo in enumerate(winning_combos):
      for j,point in enumerate(combo):
        new_combos[i][j] = (point[0])+(point[1]*16)+(point[2]*4)

    for i,x in enumerate(new_combos):
      new_combos[i] = tuple(x)

    winning_combos = new_combos

    print(winning_combos)

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self):
      self.squares = [None for i in range(64)]
      self.difficulty = 1
      self.heuristic = 0

    def show(self):
      print (self.squares[0:4])
      print (self.squares[4:8])
      print (self.squares[8:12])
      print (self.squares[12:16])

      print ("")
      print (self.squares[16:20])
      print (self.squares[20:24])
      print (self.squares[24:28])
      print (self.squares[28:32])

      print ("")
      print (self.squares[32:36])
      print (self.squares[36:40])
      print (self.squares[40:44])
      print (self.squares[44:48])
      print ("")

      print (self.squares[48:52])
      print (self.squares[52:56])
      print (self.squares[56:60])
      print (self.squares[60:64])


    def available_moves(self):
      self.availableMoves = []
      for i in range(64):
        if self.squares[i] == None:
          self.availableMoves.append(i)
      return self.availableMoves


    def heuristic_calc(self):
      xWins = 0
      oWins = 0
      plus_minus = 0

      # two nearly identical for loops... optimize somebody pls
      for combo in self.winning_combos:
        if any(combo): 
          if all([self.squares[x] == 'X' \
            or self.squares[x] != 'O' for x in combo]):
            xWins += int(math.pow(2.6,(sum([3 if (self.squares[x] == 'X') else 0 for x in combo]))))

      # for combo in self.winning_combos:
      #   if any(combo): 
      #     plus_minus = int((math.pow(2.6,(sum([3 if (self.squares[x] == 'O') else (-3) for x in combo])))))


      #      if all([self.squares[x] == 'X' \
      # #       or self.squares[x] != 'O' for x in combo]):


      for combo in self.winning_combos:
        if any(combo):
          if all([self.squares[x] == 'O' \
            or self.squares[x] != 'X' for x in combo]):
            oWins += int(math.pow(2.6,(sum([3 if (self.squares[x] == 'O') else 0 for x in combo])))) 


      return (oWins-xWins)
      # return plus_minus 

    def complete(self):
      if None not in [v for v in self.squares]:
        return True
      if self.winner() != None:
        return True
      return False

    def winner(self):
      for player in ('X', 'O'):
        positions = self.get_squares(player)
        for combo in self.winning_combos:
          win = True
          for pos in combo:
            if pos not in positions:
              win = False
          if win:
            print(combo)
            return player
      return None

    def get_squares(self, player):
      """squares that belong to a player"""
      return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
      self.squares[position] = player

if __name__ == "__main__":

    board = TicTacToe3D()
    board.show()
    # board.visualize3D()
    AI = AI(board)

    while not board.complete():
        player = 'X'
        player_move = int(input("Next Move: ")) - 1
        if not player_move in board.available_moves():
            continue
        board.make_move(player_move, player)
        board.show()

        if board.complete():
            break
        player = AI.get_enemy(player)
        computer_move = AI.determineMove(board, player)
        board.make_move(computer_move, player)
        board.show()
    print ("winner is", board.winner())