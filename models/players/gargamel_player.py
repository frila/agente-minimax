class Gargamel:
    BLACK, WHITE = '@', 'o'

    # SETAR O VALOR DE INFINITO E DE -INFINITO
    INF, NINF = 100000, -100000

    #IMPLEMENTAR
    def heuristic(self, board, move, color):
        table = [
            [120, -20, 20, 5, 5, 20, -20, 120],
            [-20, -40, -5, -5, -5, -5, -40, -20],
            [20, -5, 15, 3, 3, 15, -5, 20],
            [5, -5, 3, 3, 3, 3, -5, 5],
            [5, -5, 3, 3, 3, 3, -5, 5],
            [20, -5, 15, 3, 3, 15, -5, 20],
            [-20, -40, -5, -5, -5, -5, -40, -20],
            [120, -20, 20, 5, 5, 20, -20, 120]
        ]
        return table[move.x-1][move.y-1]

    def _can_play_in_corner(self, moves):
        vector = [ [x.x, x.y] for x in moves]
        mov = None
        r = False
        for v in vector:
            if [1,1] == v or [1,8] == v or [8,1] == v or [8,8] == v:
                moves[0].x = v[0]
                moves[0].y = v[1]
                return True, moves[0]

            if [3,3] == v or [3,6] == v or [6,6] == v or [6,3] == v:
                moves[0].x = v[0]
                moves[0].y = v[1]
                r = True

        return r, moves[0]


    def __init__(self, color):
        self.color = color
        self.color_me = color

        if color == Gargamel.BLACK:
            self.color_challenger = Gargamel.WHITE
        else:
            self.color_challenger = Gargamel.BLACK

    def play(self, board):
        depth = 6
        return self.minimax(board, depth)

    def minimax(self, board, depth):
        if depth <= 0:
            raise Exception('Depth invalid value')

        v = self._can_play_in_corner(board.valid_moves(self.color_me))

        if v[0]:
            return v[1]

        heuristic_value, best_move = self.function_max(board, depth, self.color_me, None, [], [])

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
            parent_min_to_pass = None
            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                if heuristic_value is None:
                    parent_to_pass = parent_max[:]
                    parent_min_to_pass = parent_min[:]
                else:
                    if self.check_cut_min(parent_min, heuristic_value):
                        break
                    parent_to_pass = parent_max[:-1]

                new_heuristic_value = self.function_min(board_clone, depth - 1, self._change_color(color), move, parent_to_pass, parent_min_to_pass)[0]

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

            parent_max_to_pass = None
            for move in valid_moves:
                board_clone = board.get_clone()
                board_clone.play(move, color)

                if heuristic_value is None:
                    parent_to_pass = parent_min[:]
                    parent_max_to_pass = parent_max[:]
                else:
                    if self.check_cut_max(parent_max, heuristic_value):
                        break
                    parent_to_pass = parent_min[:-1]

                new_heuristic_value = self.function_max(board_clone, depth - 1, self._change_color(color), move, parent_max_to_pass, parent_to_pass)[0]

                if heuristic_value is None or new_heuristic_value < heuristic_value:
                    if heuristic_value is not None:
                        parent_min.pop()
                    parent_min.append(new_heuristic_value)
                    heuristic_value = new_heuristic_value
                    best_move = move

            return heuristic_value, best_move
