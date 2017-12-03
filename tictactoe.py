import random
from minimax import AI

class Tic():
    winning_combos = (
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6])

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self):
      self.squares = [None for i in range(9)]

    def show(self):
      print (self.squares[0:3])
      print (self.squares[3:6])
      print (self.squares[6:9])

    def available_moves(self):
      self.availableMoves = []
      for i in range(9):
        if self.squares[i] == None:
          self.availableMoves.append(i)

      return self.availableMoves

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
    board = Tic()
    board.show()
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
        computer_move = AI.determine(board, player)
        board.make_move(computer_move, player)
        board.show()
    print ("winner is", board.winner())