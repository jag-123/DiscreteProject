class TicTacToe():

	def __init__(self):
		self.squares={}
		self.winningNumbers = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])
		self.player = "x"

	def createBoard(self):
		for i in range(9):
			self.squares[i]="_"

	def drawBoard(self):
		print ()
		print(self.squares[0], self.squares[1], self.squares[2])
		print(self.squares[3], self.squares[4], self.squares[5])
		print(self.squares[6], self.squares[7], self.squares[8])

	def getAvailableMoves(self):


	def makeMove(self, position):
		if self.squares[position] == "_":
			self.squares[position] = self.player

		if self.player == "x":
			self.player = "o"
		else:
			self.player = "x"

		self.drawBoard()

	def getWinner(self):
		for player in ("x", "o"):
			for win in self.winningNumbers:
				if self.squares[win[0]] == player and self.squares[win[1]] == player and self.squares[win[2]] == player:
					return player

		if "_" not in self.squares.values():
			return "tie"

if __name__ == '__main__':
	game = TicTacToe()
	game.createBoard()
	game.makeMove(1)
	game.makeMove(2)
	game.makeMove(4)
	game.makeMove(6)
	game.makeMove(7)
	game.getWinner()