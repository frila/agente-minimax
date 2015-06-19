from models.board import Board


class Heuristic:

  def heuristic(self, board):
    raise NotImplementedError('Dont override this class')

  #Se a função eval retornar false irá trocar o valor de old_value por new_value. Se retornar valor true nao trocará
  #old_value e new_value são valores heuristico encontrado no decorrer do cálculo
  def eval(self, old_value, new_value):
    raise NotImplementedError('Dont override this class')

###################################   
# NÃO RELAR A MÃO NESSAS CLASSES, #
# CASO NAO TENHA CERTEZA DO QUE   #
# ESTA FAZENDO                    #
###################################


class MinimaxPlayer:
  def __init__(self, color, depth, heuristic_me, heuristic_challenger):
    self.depth = depth
    self.color = color
    self.heuristic_me.color = color

    if color == Board.BLACK:
      self.heuristic_challenger.color = Board.WHITE
    else:
      self.heuristic_challenger.color = Board.BLACK
    
    self.minimax = Minimax(self.heuristic_me,self.heuristic_challenger)
    
  def play(self, board):
    return self.minimax.call_minimax(board,self.depth);

class Minimax:
  def __init__(self, me, challenger):
    self.me, self.challenger = me, challenger

  def call_minimax(self, board, depth):
    if depth <= 0:
      raise Exception('Depth invalid value')

    heuristic_value, best_move = self._minimax(board,depth, self.me, None)
    
    if best_move == None:
      raise Exception('Depth invalid value or you do merda!!!!')

    return best_move

  # Privates Methods
  def _change_color(self, color):
    if color == self.me.color:
      return self.challenger
    else:
      return self.me

  def _valid_moves(self, board, color):
    return board.valid_moves(color.color)

  def _clone_board(self, board):
    return board.get_clone()

  # Depth não pode ser <= 0
  # Retorna (valor_heuristico, movimento)
  # TODO: Pensar para situação quando nao tem jogada
  # TODO: Pensar para o caso de encontrar a vitoria antes de terminar a profundidade
  def _minimax(self, board, depth, color, move):
    if depth == 0:
      return self.color.heuristic(board), move
    
    else:
      valid_moves = self.valid_moves(board, color)
      heuristic_value = None
      best_move = None

      for move in valid_moves:
        board_clone = self.clone_board(board)
        self.board.play(move, color)
        
        new_heuristic_value = self.minimax(board_clone, depth-1, self.change_color(color))[0]

        elif heuristic_value is None or not color.eval(heuristic_value, new_heuristic_value):          
          heuristic_value = new_heuristic_value
          best_move = move

      return heuristic_value, best_move

