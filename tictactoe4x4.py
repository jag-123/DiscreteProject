import random
from minimax import AI

class TicTacToe3D():
    winning_combos = (
      (51, 50, 49, 48), (55, 54, 53, 52), (59, 58, 57, 56), (63, 62, 61, 60), (35, 34, 33, 32), (39, 38, 37, 36), (43, 42, 41, 40), (47, 46, 45, 44), (19, 18, 17, 16), (23, 22, 21, 20), (27, 26, 25, 24), (31, 30, 29, 28), (3, 2, 1, 0), (7, 6, 5, 4), (11, 10, 9, 8), (15, 14, 13, 12), (51, 55, 59, 63), (50, 54, 58, 62), (49, 53, 57, 61), (48, 52, 56, 60), (35, 39, 43, 47), (34, 38, 42, 46), (33, 37, 41, 45), (32, 36, 40, 44), (19, 23, 27, 31), (18, 22, 26, 30), (17, 21, 25, 29), (16, 20, 24, 28), (3, 7, 11, 15), (2, 6, 10, 14), (1, 5, 9, 13), (0, 4, 8, 12), (51, 54, 57, 60), (63, 58, 53, 48), (35, 38, 41, 44), (47, 42, 37, 32), (19, 22, 25, 28), (31, 26, 21, 16), (3, 6, 9, 12), (15, 10, 5, 0), (51, 35, 19, 3), (50, 34, 18, 2), (49, 33, 17, 1), (48, 32, 16, 0), (55, 39, 23, 7), (54, 38, 22, 6), (53, 37, 21, 5), (52, 36, 20, 4), (59, 43, 27, 11), (58, 42, 26, 10), (57, 41, 25, 9), (56, 40, 24, 8), (63, 47, 31, 15), (62, 46, 30, 14), (61, 45, 29, 13), (60, 44, 28, 60), (51, 38, 25, 12), (63, 42, 21, 0)

    )

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self):
      self.squares = [None for i in range(64)]
      self.difficulty = 2
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

      #two nearly identical for loops... optimize somebody pls
      for combo in self.winning_combos:
        if all([self.squares[x] == 'X' \
          or self.squares[x] != 'O' for x in combo]):
          xWins += 1   

      for combo in self.winning_combos:
        if all([self.squares[x] == 'O' \
          or self.squares[x] != 'X' for x in combo]):
          oWins += 1            

      self.heuristic = (oWins-xWins)

      return (oWins-xWins)

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