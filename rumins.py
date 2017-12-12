  def computers_move(self):
        """Initiates the process of attempting to find the best (or decent)
        move possible from the available positions on the board."""

        best_score = -1000
        best_move = None
        h = None
        win = False

        for move in self.allowed_moves:
            self.move(move, self.ai)
            if self.complete:
                win = True
                break
            else:
                h = self.think_ahead(self.human, -1000, 1000)
                self.depth_count = 0
                if h >= best_score:
                    best_score = h
                    best_move = move
                    self.undo_move(move)
                else:
                    self.undo_move(move)
                
                # see if it blocks the player
                self.move(move, self.human)
                if self.complete and self.winner == self.human:
                    if 1001 >= best_score:
                        best_score = 1001
                        best_move = move
                self.undo_move(move)

        if not win:
            self.move(best_move, self.ai)
        self.human_turn = True