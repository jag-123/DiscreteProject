import random

class AI():
    def __init__(self,board):
        self.board = board
        self.maximizingPlayer = None

    def determineMove(self, board, player):
        best_score = -10000
        choices = []
        best_move = None
        self.maximizingPlayer = player

        for move in board.available_moves():
            if board.complete() and (board.winner() == player):
                return move
            else:
                board.make_move(move, player)
                val = self.alphabeta(board, self.get_enemy(player), -10000, 10000, 0)
                board.make_move(move, None)
                print ("move:", move+1, "heuristic:", val)
                if val >= best_score:
                    best_score = val
                    best_move = move
            board.make_move(move,self.get_enemy(player))
            if board.complete() and (board.winner() == (self.get_enemy(player))):
                if 10001 >= best_score:
                    best_score = 10001
                    best_move = move
            board.make_move(move,None)

        #currently only returns first 'best' move
        return best_move

    def alphabeta(self, node, player, alpha, beta, depth):


        if depth == node.difficulty:
            return node.heuristic_calc(self.maximizingPlayer)

        if player == self.maximizingPlayer:
            for move in node.available_moves():
                node.make_move(move, player)

                #check for winner
                if node.complete() and node.winner == self.maximizingPlayer:
                    node.make_move(move,None)
                    return 10000

                val = self.alphabeta(node, self.get_enemy(player), alpha, beta, depth+1)
                node.make_move(move, None)

                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            return alpha

        if player != self.maximizingPlayer:
            for move in node.available_moves():
                node.make_move(move, player)

                #check for winner
                if node.complete() and node.winner == self.get_enemy(player):
                    node.make_move(move,None)
                    return -10000

                val = self.alphabeta(node, self.get_enemy(player), alpha, beta, depth+1)
                node.make_move(move, None)


                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
            return beta



        if player == self.maximizingPlayer:
            return alpha
        else:
            return beta

    def get_enemy(self, player):
        if player == 'X':
            return 'O'
        return 'X'