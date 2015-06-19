from models.board import Board

class Heuristic:
  def __init__(self, color):
    self.color = color

  def heuristic(self, board):
    raise NotImplementedError('Dont override this class')

  #Se a função eval retornar false irá trocar o valor de old_value por new_value. Se retornar valor true nao trocará
  #old_value e new_value são valores heuristico encontrado no decorrer do cálculo
  def eval(self, old_value, new_value):
    raise NotImplementedError('Dont override this class')


class Minimax:
  def __init__(self, me, challenger):
    self.me, self.challenger = me, challenger

  def change_color(self, color):
    if color == self.me.color:
      return self.challenger.color
    else:
      return self.me.color

  def valid_moves(self, board, color):
    return board.valid_moves(color.color)

  def clone_board(self, board):
    return board.get_clone()

  # Depth não pode ser <= 0
  # Retorna (valor_heuristico, movimento)
  def minimax(self, board, depth, color, move):
    if depth == 0:
      return self.color.heuristic(board)
    
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
      
