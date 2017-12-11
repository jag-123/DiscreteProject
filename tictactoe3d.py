import random
from minimax import AI

class TicTacToe3D():
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14],
        [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26],

        [0, 3, 6], [1, 4, 7], [2, 5, 8], [9, 12, 15], [10, 13, 16],
        [11, 14, 17], [18, 21, 24], [19, 22, 25], [20, 23, 26],

        [0, 4, 8], [2, 4, 6], [9, 13, 17], [11, 13, 15], [18, 22, 26],
        [20, 22, 24],

        [0, 9, 18], [1, 10, 19], [2, 11, 20], [3, 12, 21], [4, 13, 22],
        [5, 14, 23], [6, 15, 24], [7, 16, 25], [8, 17, 26],

        [0, 12, 24], [1, 13, 25], [2, 14, 26], [6, 12, 18], [7, 13, 19],
        [8, 14, 20], [0, 10, 20], [3, 13, 23], [6, 16, 26], [2, 10, 18],
        [5, 13, 21], [8, 16, 24], [0, 13, 26], [2, 13, 24], [6, 13, 20],
        [8, 13, 18]
    )

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self):
      self.squares = [None for i in range(27)]
      self.difficulty = 5
      self.heuristic = 0

    def show(self):
      print (self.squares[0:3])
      print (self.squares[3:6])
      print (self.squares[6:9])
      print ("")
      print (self.squares[9:12])
      print (self.squares[12:15])
      print (self.squares[15:18])
      print ("")
      print (self.squares[18:21])
      print (self.squares[21:24])
      print (self.squares[24:27])


    def visualize3D(self):
      print("                 ________________")
      print("                / {0} /   /   / O /|".format("X"))
      print("               /___/___/___/___/ |")
      print("              / O / X /   / X /  |")
      print("             /___/___/___/___/   |")
      print("            /   / O / X / O /    |")
      print("           /___/___/___/___/     |")
      print("          /   /   /   / O /      |")
      print("         /___/___/___/___/       |")
      print("        |       |________|_______|")
      print("        |       /   /   /|O /   /|")
      print("        |      /___/___/_|_/___/ |")
      print("        |     / X / X / O|/ X /  |")
      print("        |    /___/___/___|___/   |")
      print("        |   /   / O / O /|  /    |")
      print("        |  /___/___/___/_|_/     |")
      print("        | /   /   / O /  |/      |")
      print("        |/___/___/___/___|       |")
      print("        |       |________|_______|")
      print("        |       / X / O /|  /   /|")
      print("        |      /___/___/_|_/___/ |")
      print("        |     / X / X / O|/   /  |")
      print("        |    /___/___/___|___/   |")
      print("        |   /   / O / X /|  /    |")
      print("        |  /___/___/___/_|_/     |")
      print("        | /   /   /   / X|/      |")
      print("        |/___/___/___/___|       |")
      print("        |       |________|_______|")
      print("        |       / O /   /|  /   /")
      print("        |      /___/___/_|_/___/")
      print("        |     / X / X / X|/ X /")
      print("        |    /___/___/___|___/")
      print("        |   / O / O /   /|  /")
      print("        |  /___/___/___/_|_/")
      print("        | / O /   /   / X|/")
      print("        |/___/___/___/___|")


    def available_moves(self):
      self.availableMoves = []
      for i in range(27):
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