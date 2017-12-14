from tictactoe4x4 import TicTacToe3D
from minimax2 import AI

class AIvsAI():

	def __init__(self,xIQ = 2,oIQ = 2):
		self.board = TicTacToe3D()
		self.AI = AI(self.board)
		self.xIQ = xIQ
		self.oIQ = oIQ

	def GameRunner(self):
		done = False
		player = "O"

		#resets for each game
		self.board = TicTacToe3D()
		self.AI = AI(self.board)

		while not done:
			player = self.AI.get_enemy(player)

			#make x smarter...
			if player == "X":
				self.board.difficulty = self.xIQ
			else:
				self.board.difficulty = self.oIQ

			#make move for current player
			computer_move = self.AI.determineMove(self.board, player)
			self.board.make_move(computer_move, player)

			#print board and move
			# self.board.show()
			# print(player, computer_move)
			# print("")

			if self.board.complete():
				print('done')
				print("winner is", self.board.winner())
				done = True

		return self.board.winner()



if __name__ == '__main__':
	game = AIvsAI(1,1)

	xWins = 0
	yWins = 0
	tie = 0
	for i in range(100):
		winner = game.GameRunner()
		if winner == "X":
			xWins = xWins + 1
		elif winner == "O":
			oWins = oWins + 1
		else:
			tie = tie + 1
