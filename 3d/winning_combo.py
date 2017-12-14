winning_combo = [
[[3,3,0], [2,3,0], [1,3,0], [0,3,0]], [[3,3,1], [2,3,1], [1,3,1], [0,3,1]], [[3,3,2], [2,3,2], [1,3,2], [0,3,2]], [[3,3,3], [2,3,3], [1,3,3], [0,3,3]],
[[3,2,0], [2,2,0], [1,2,0], [0,2,0]], [[3,2,1], [2,2,1], [1,2,1], [0,2,1]], [[3,2,2], [2,2,2], [1,2,2], [0,2,2]], [[3,2,3], [2,2,3], [1,2,3], [0,2,3]],
[[3,1,0], [2,1,0], [1,1,0], [0,1,0]], [[3,1,1], [2,1,1], [1,1,1], [0,1,1]], [[3,1,2], [2,1,2], [1,1,2], [0,1,2]], [[3,1,3], [2,1,3], [1,1,3], [0,1,3]],
[[3,0,0], [2,0,0], [1,0,0], [0,0,0]], [[3,0,1], [2,0,1], [1,0,1], [0,0,1]], [[3,0,2], [2,0,2], [1,0,2], [0,0,2]], [[3,0,3], [2,0,3], [1,0,3], [0,0,3]],
[[3,3,0], [3,3,1], [3,3,2], [3,3,3]], [[2,3,0], [2,3,1], [2,3,2], [2,3,3]], [[1,3,0], [1,3,1], [1,3,2], [1,3,3]], [[0,3,0], [0,3,1], [0,3,2], [0,3,3]],
[[3,2,0], [3,2,1], [3,2,2], [3,2,3]], [[2,2,0], [2,2,1], [2,2,2], [2,2,3]], [[1,2,0], [1,2,1], [1,2,2], [1,2,3]], [[0,2,0], [0,2,1], [0,2,2], [0,2,3]],
[[3,1,0], [3,1,1], [3,1,2], [3,1,3]], [[2,1,0], [2,1,1], [2,1,2], [2,1,3]], [[1,1,0], [1,1,1], [1,1,2], [1,1,3]], [[0,1,0], [0,1,1], [0,1,2], [0,1,3]],
[[3,0,0], [3,0,1], [3,0,2], [3,0,3]], [[2,0,0], [2,0,1], [2,0,2], [2,0,3]], [[1,0,0], [1,0,1], [1,0,2], [1,0,3]], [[0,0,0], [0,0,1], [0,0,2], [0,0,3]],
#horizontal diagonal
[[3,3,0],[2,3,1],[1,3,2],[0,3,3]],[[3,3,3],[2,3,2],[1,3,1],[0,3,0]],[[3,2,0],[2,2,1],[1,2,2],[0,2,3]],[[3,2,3],[2,2,2],[1,2,1],[0,2,0]],[[3,1,0],[2,1,1],[1,1,2],[0,1,3]],[[3,1,3],[2,1,2],[1,1,1],[0,1,0]], [[3,0,0],[2,0,1],[1,0,2],[0,0,3]], [[3,0,3],[2,0,2],[1,0,1],[0,0,0]],
#vertical
[[3,3,0],[3,2,0],[3,1,0],[3,0,0]],[[2,3,0],[2,2,0],[2,1,0],[2,0,0]],[[1,3,0],[1,2,0],[1,1,0],[1,0,0]],[[0,3,0],[0,2,0],[0,1,0],[0,0,0]],
[[3,3,1],[3,2,1],[3,1,1],[3,0,1]],[[2,3,1],[2,2,1],[2,1,1],[2,0,1]],[[1,3,1],[1,2,1],[1,1,1],[1,0,1]],[[0,3,1],[0,2,1],[0,1,1],[0,0,1]],
[[3,3,2],[3,2,2],[3,1,2],[3,0,2]],[[2,3,2],[2,2,2],[2,1,2],[2,0,2]],[[1,3,2],[1,2,2],[1,1,2],[1,0,2]],[[0,3,2],[0,2,2],[0,1,2],[0,0,2]],
[[3,3,3],[3,2,3],[3,1,3],[3,0,3]],[[2,3,3],[2,2,3],[2,1,3],[2,0,3]],[[1,3,3],[1,2,3],[1,1,3],[1,0,3]],[[0,3,3],[0,2,3],[0,1,3],[0,3,3]],
#diagonal diagonal - 2 missing here
[[3,3,0],[2,2,1],[1,1,2],[0,0,3]],[[3,3,3],[2,2,2],[1,1,1],[0,0,0]]
]
#add vertical diagonal - 16

print (len(winning_combo))

new_combos = winning_combo[:]

for i,combo in enumerate(winning_combo):
  for j,point in enumerate(combo):
    new_combos[i][j] = (point[0])+(point[1]*16)+(point[2]*4)

for i,x in enumerate(new_combos):
	new_combos[i] = tuple(x)

print (new_combos)