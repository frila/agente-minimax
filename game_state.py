#include board

class GameState:
  def __init__(self, board):
    self.board = board

  def apply_move(self, move, color):
    self.board.play(move, color)
    # self.number_of_moves = len(board.valid_moves())

  def remove_move(self, move):
    self.board.board[move.x][move.y] = Board.EMPTY

  def change_color(self):
    if self.color == Board.BLACK:
      self.color = Board.WHITE
    else
      self.color = Board.BLACK