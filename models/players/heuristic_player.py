class HeuristicPlayer:
  BLACK, WHITE = '@', 'o'

  #SETAR O VALOR DE INFINITO E DE -INFINITO
  INF, NINF = 1000,-1000

  #IMPLEMENTAR
  def evalMe(self, old_value, new_value):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    return old_value > new_value # isso representa o max

  #IMPLEMENTAR
  def evalChallenge(self, old_value, new_value):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    return old_value < new_value # isso representa o min

  #IMPLEMENTAR
  def heuristic(self, board):
    return 1

  def __init__(self, color):
    self.color = color
    self.color_me = color

    if color == HeuristicPlayer.BLACK:
        self.color_challenger = HeuristicPlayer.WHITE
    else:
        self.color_challenger = HeuristicPlayer.BLACK

  def play(self, board):
    depth = 5
    return self.call_minimax(board, depth)

  def call_minimax(self, board, depth):
    if depth <= 0:
        raise Exception('Depth invalid value')

    heuristic_value, best_move = self._minimax(board, depth, self.color_me, None)

    if best_move == None:
        raise Exception('Depth invalid value or you do merda!!!!')

    return best_move

   # Privates Methods
  def _change_color(self, color):
    if color == self.color_me:
        return self.color_challenger
    else:
        return self.color_me

  def _valid_moves(self, board, color):
    return board.valid_moves(color)

  def _clone_board(self, board):
    return board.get_clone()

  def _eval(self,color, old_value, new_value):
    if color == self.color_me:
        return self.evalMe(old_value,new_value)
    else:
        return self.evalChallenge(old_value,new_value)
  

  # Depth nao pode ser <= 0
  # Retorna (valor_heuristico, movimento)
  # TODO: fazer poda
  def _minimax(self, board, depth, color, move):
    if depth == 0:
      return self.heuristic(board), move

    else:
      valid_moves = self._valid_moves(board, color)
      heuristic_value = None
      best_move = None

      if len(valid_moves) is 0:
        return self.heuristic(board)

      for move in valid_moves:
        board_clone = self._clone_board(board)
        board_clone.play(move, color)

        new_heuristic_value = self._minimax(board_clone, depth - 1, self._change_color(color), move)[0]

        if heuristic_value is None or not self._eval(color, heuristic_value, new_heuristic_value):
          heuristic_value = new_heuristic_value
          best_move = move

      return heuristic_value, best_move

