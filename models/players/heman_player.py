class Heman:
  BLACK, WHITE = '@', 'o'

  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.heuristic(board.valid_moves(self.color), board)

  def heuristic(self, moves, board):
    number_of_moves = 100
    avoid_moves = []
    good_moves = []

    for move in moves:
      if self._is_corner([move.x, move.y]):
        return move

      board_clone = board.get_clone()
      board_clone.play(move, self.color)
      next_moves = board_clone.valid_moves(self._challenger_color(self.color))
      
      if(len(next_moves) <= number_of_moves and not self._is_corner_neighbour([move.x, move.y])):
        number_of_moves = len(next_moves)
        good_moves.append((move, self._score_of_move(board_clone)))
      
      if(self._is_corner_neighbour([move.x, move.y])):
        avoid_moves.append(move)

    # if(len(avoid_moves) == len(moves)):
    #   best_move = moves[0]
    if(len(good_moves) > 0):
      current_score = 0
      best_move = None
      for m in good_moves:
        if m[1] > current_score:
          current_score = m[1]
          best_move = m[0]
      return best_move
    else:
      return self._get_best_avoid(avoid_moves)

  def _get_best_avoid(self, avoid_moves):
    best_avoid_moves = []
    for move in avoid_moves:
      if [move.x, move.y] not in [ [2,2], [2,7], [7,2], [7,7]]:
        best_avoid_moves.append(move)
    
    if ( len(best_avoid_moves) > 0 ):
      return best_avoid_moves[0]
    else:
      return avoid_moves[0]

  def _is_corner(self, position):
    return position in [[1,1], [1,8], [8,1], [8,8]]

  def _is_corner_neighbour(self, position):
    return position in [[1,2],[2,1],[2,2],[1,7],[2,7],[2,8],[7,1],[7,2],[8,1],[7,7],[7,8],[8,7]]

  def _score_of_move(self, board):
    return board.score()[self._get_index_of_color()]

  def _get_index_of_color(self):
    if(self.color == Heman.WHITE):
      return 0
    return 1

  def _challenger_color(self, color):
    if color == Heman.BLACK:
      return Heman.WHITE
    else:
      return Heman.BLACK