class Heuristic:

  def heuristic(self, board, color):
    raise NotImplementedError('Dont override this class')


class Minimax:
  def __init__(self, color_me, h_me, h_challenger):
    self.h_me = h_me
    self.h_challenger = h_challenger
    self.color_me = color_me

  

  def heuristic(self, board, color):
    if color == self.color_me:
      return self.h_me.heuristic(board, color)
    else
      return self.h_challenger.heuristic(board, color)