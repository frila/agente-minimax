class HemanPlayer:
    BLACK, WHITE = '@', 'o'

    # SETAR O VALOR DE INFINITO E DE -INFINITO
    INF, NINF = 1000, -1000

    #IMPLEMENTAR
    def heuristic(self, board, move, color):
        return len(board.valid_moves(color))    

    def __init__(self, color):
        self.color = color
        self.color_me = color

        if color == HemanPlayer.BLACK:
            self.color_challenger = HemanPlayer.WHITE
        else:
            self.color_challenger = HemanPlayer.BLACK

    def play(self, board):
        depth = 5
        return self.minimax(board, depth)

    def minimax(self, board, depth):
        if depth <= 0:
            raise Exception('Depth invalid value')

        heuristic_value, best_move = self.function_max(board, depth, self.color_me, None,[],[])

        if best_move is None:
            raise Exception('Depth invalid value or you do merda!!!!')

        return best_move

    # Privates Methods

    def _change_color(self, color):
        if color == self.color_me:
            return self.color_challenger
        else:
            return self.color_me

    def check_cut_max(self, parent_max, new_value):
        if len(parent_max) > 0:
            for x in parent_max:
                if new_value <= x:
                    return True
        return False

    def check_cut_min(self, parent_min, new_value):
        if len(parent_min) > 0:
            for x in parent_min:
                if new_value >= x:
                    return True
        return False

    def function_max(self, board, depth, color, m, parent_max, parent_min):
        if depth == 0:
            return self.heuristic(board, m, color), m
        else:
            valid_moves = board.valid_moves(color)
            heuristic_value = None
            best_move = None

            if len(valid_moves) is 0:
                return self.heuristic(board, m, color), m

            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                if heuristic_value is None:
                    parent_to_pass = parent_max[:]
                else:
                    if self.check_cut_min(parent_min, heuristic_value):
                        break
                    parent_to_pass = parent_max[:-1]

                new_heuristic_value = self.function_min(board_clone, depth - 1, self._change_color(color), move, parent_to_pass, parent_min)[0]

                if heuristic_value is None or new_heuristic_value < heuristic_value:
                    if heuristic_value is not None:
                        parent_max.pop()
                    parent_max.append(new_heuristic_value)
                    heuristic_value = new_heuristic_value
                    best_move = move

            return heuristic_value, best_move

    def function_min(self, board, depth, color, m, parent_max, parent_min):
        if depth == 0:
            return self.heuristic(board, m, color), m
        else:
            valid_moves = board.valid_moves(color)
            heuristic_value = None
            best_move = None

            if len(valid_moves) is 0:
                return self.heuristic(board, m, color), m

            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                if heuristic_value is None:
                    parent_to_pass = parent_min[:]
                else:
                    if self.check_cut_max(parent_max, heuristic_value):
                        break
                    parent_to_pass = parent_min[:-1]

                new_heuristic_value = self.function_max(board_clone, depth - 1, self._change_color(color), move, parent_max, parent_to_pass)[0]

                if heuristic_value is None or new_heuristic_value < heuristic_value:
                    if heuristic_value is not None:
                        parent_min.pop()
                    parent_min.append(new_heuristic_value)
                    heuristic_value = new_heuristic_value
                    best_move = move

            return heuristic_value, best_move
