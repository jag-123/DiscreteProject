def minimax(node, depth, maximizingPlayer):
	if depth = 0 or node is a terminal node
		return the heuristic value of node

	if maximizingPlayer
		bestValue = float('-inf')
		for each child of node
			v := minimax(child, depth − 1, FALSE)
			bestValue := max(bestValue, v)
		return bestValue

	else
		bestValue = float('inf')
		for each child of node
			v := minimax(child, depth − 1, TRUE)
			bestValue := min(bestValue, v)
	return bestValue