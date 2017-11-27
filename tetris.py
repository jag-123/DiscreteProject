"""
Tetris AI written by Willem Thorbecke, Sungwoo Park, and Jeremy Garcia.
"""
columns = 10
rows = 22

class TetrisApp():
	def __init__(self,columns,rows):
		self.grid = [[None for x in range(columns)] for y in range(rows)]
		self.grid += [[ 1 for x in range(columns)]]

test = TetrisApp(columns, rows)

for row in test.grid:
	s = ''
	for item in row:
		if item is None:
			s += ' '
		else:
			s += 'X'
	print(s)