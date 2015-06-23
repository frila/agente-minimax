class Heman:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.heuristic(board.valid_moves(self.color))

  def heuristic(self, moves):
    number_of_moves = 0
    avoid_moves = []

    for move in moves:
      if self._is_corner([move.x, move.y]):
        return move

      if(len(moves) > number_of_moves and not self._is_corner_neighbour([move.x, move.y])):
        number_of_moves = len(moves)
        best_move = move
      
      if(self._is_corner_neighbour([move.x, move.y])):
        avoid_moves.append(move)

    if(len(avoid_moves) == len(moves)):
      best_move = moves[0]

    return best_move

  def _is_corner(self, position):
    return position in [[1,1], [1,8], [8,1], [8,8]]

  def _is_corner_neighbour(self, position):
    return position in [[1,2],[2,1],[2,2],[1,7],[2,7],[2,8],[7,1],[7,2],[8,1],[7,7],[7,8],[8,7]]
