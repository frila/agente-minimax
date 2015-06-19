from models.algorithm.minimax import Heuristic
from models.algorithm.minimax import Minimax
from models.board import Board
import random

class HeuristicTestBlack(Heuristic):

  def __init__(self):
    Heuristic.__init__(Board.BLACK)

  def heuristic(self, board, color):
    return random.randrange(-20, 20)

  def eval(self, vector):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    #return max(vector)
    return min(vector)

class HeuristicTestWhite(Heuristic):

  def __init__(self):
    Heuristic.__init__(Board.WHITE)

  def heuristic(self, board, color):
    return random.randrange(-20, 20)

  def eval(self, vector):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    return max(vector)
    #return min(vector)