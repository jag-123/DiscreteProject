import random

class AI():
    def __init__(self,board):
        self.board = board

    def determineMove(self, board, player):
        a = -2
        choices = []
        if len(board.available_moves()) == 9:
            return 4
        for move in board.available_moves():
            board.make_move(move, player)
            val = self.alphabeta(board, self.get_enemy(player), -2, 2, 0)
            board.make_move(move, None)
            print ("move:", move+1, "heuristic:", val)
            # print ("move:", move + 1, "causes:", board.winners[val + 1], board.heuristic)
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
        return random.choice(choices)

    def alphabeta(self, node, player, alpha, beta, depth):


        if depth == node.difficulty:
            return node.heuristic_calc()

        if node.complete():
            if node.winner() == 'X':
                return -1000
            elif node.complete() == True and node.winner() is None:
                return 0
            elif node.winner() == 'O':
                return 1000

        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, self.get_enemy(player), alpha, beta, depth+1)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta

    def get_enemy(self, player):
        if player == 'X':
            return 'O'
        return 'X'