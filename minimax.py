class Heuristic:

  def __init__(self, color):
    self.color = color

  def heuristic(self, board, color):
    raise NotImplementedError('Dont override this class')

  def eval(self, vector):
    raise NotImplementedError('Dont override this class')
    

class Minimax:
  def __init__(self, me, challenger):
    self.me = me
    self.challenger = challenger

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
