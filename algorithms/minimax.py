def mimax(game_state):
  if game_state.depth == 0 :
    heuristic()
  else:
    leng = game_state.board.valid_move()
    for :
      apply_move
      mimax
      remove_move

def change_color(color):
  if color == Board.BLACK:
    return Board.WHITE
  else
    return Board.BLACK

def minimax(game_state, depth, color, move):
  if depth == 0:
    heuristic()
  else:
    valid_moves = game_state.board.valid_moves()
    for move in valid_moves:
      game_state.apply_move(move, color)
      minimax(game_state, depth, color, move)