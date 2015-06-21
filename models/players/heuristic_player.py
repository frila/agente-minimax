class HeuristicPlayer:
    BLACK, WHITE = '@', 'o'

    # SETAR O VALOR DE INFINITO E DE -INFINITO
    INF, NINF = 1000, -1000

    #IMPLEMENTAR
    def heuristic(self, board, move):
        return 1

    def __init__(self, color):
        self.color = color
        self.color_me = color
        self.min_stack, self.max_stack = {}, {}

        if color == HeuristicPlayer.BLACK:
            self.color_challenger = HeuristicPlayer.WHITE
        else:
            self.color_challenger = HeuristicPlayer.BLACK

    def play(self, board):
        depth = 5
        return self.minimax(board, depth)

    def minimax(self, board, depth):
        self.min_stack, self.max_stack = {}, {}
        if depth <= 0:
            raise Exception('Depth invalid value')

        heuristic_value, best_move = self.function_max(board, depth, self.color_me, None)

        if best_move is None:
            raise Exception('Depth invalid value or you do merda!!!!')

        return best_move

    # Privates Methods

    def _change_color(self, color):
        if color == self.color_me:
            return self.color_challenger
        else:
            return self.color_me

    def function_max(self, board, depth, color, m):
        if depth == 0:
            return self.heuristic(board, m), m
        else:
            valid_moves = board.valid_moves(color)
            heuristic_value = None
            best_move = None

            if len(valid_moves) is 0:
                return self.heuristic(board, m)

            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                new_heuristic_value = self.function_min(board_clone, depth - 1, self._change_color(color), move)[0]

                if heuristic_value is None or new_heuristic_value > heuristic_value:
                    heuristic_value = new_heuristic_value
                    best_move = move
                    self.max_stack[depth] = heuristic_value

            return heuristic_value, best_move

    def function_min(self, board, depth, color, m):
        if depth == 0:
            return self.heuristic(board, m), m
        else:
            valid_moves = board.valid_moves(color)
            heuristic_value = None
            best_move = None

            if len(valid_moves) is 0:
                return self.heuristic(board, m)

            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                new_heuristic_value = self.function_max(board_clone, depth - 1, self._change_color(color), move)[0]

                if heuristic_value is None or new_heuristic_value < heuristic_value:
                    heuristic_value = new_heuristic_value
                    best_move = move
                    self.max_stack[depth] = heuristic_value

            return heuristic_value, best_move
