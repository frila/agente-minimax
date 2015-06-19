class Heuristic:
  def __init__(self, color):
    self.color = color

  def heuristic(self, board, color):
    raise NotImplementedError('Dont override this class')

  def eval(self, vector):
    raise NotImplementedError('Dont override this class')


class Minimax:
  def __init__(self, me, challenger):
    self.me, self.challenger = me, challenger

  def heuristic(self, board, color):
    if color == self.color_me:
      return self.me.heuristic(board, color)
    else
      return self.challenger.heuristic(board, color)

  def calculate_min_or_max(self, vector_values, color):
    if color == self.me.color:
      return self.me.eval(vector_values)
    else:
      return self.challenger.eval(vector_values)

  def change_color(self, color):
    if color == self.me.color:
      return self.challenger.color
    else:
      return self.me.color

  def children(self, board, color):
    return board.valid_moves(color)

  def clone_board(self, board):
    return board.get_clone()

  def minimax(self, board, depth, color):
    if depth == 0:
      return self.heuristic(board,color)
    else:
      children = self.children(board, color)
      results = []
      for child in children:
        board_clone = self.clone_board(board)
        self.board.play(child, color)
        results[] = self.minimax(board_clone, depth-1, self.change_color(color))
      return self.calculate_min_or_max(vector_values, color)

