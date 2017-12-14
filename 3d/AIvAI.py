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
			self.board.show()
			print(player, computer_move)
			print("")

			if self.board.complete():
				print('done')
				print("winner is", self.board.winner())
				done = True




if __name__ == '__main__':
	game = AIvsAI(1,1)
	game.GameRunner()	