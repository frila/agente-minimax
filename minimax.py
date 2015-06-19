class Heuristic:

  def __init__(self, color):
    self.color = color

  def heuristic(self, board, color):
    raise NotImplementedError('Dont override this class')

  def eval(self, vector):
    pass

class Minimax:
  def __init__(self, me, challenger):
    self.me = me
    self.challenger = challenger

  def heuristic(self, board, color):
    if color == self.color_me:
      return self.me.heuristic(board, color)
    else
      return self.challenger.heuristic(board, color)
