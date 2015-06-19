from models.algorithm.minimax import Heuristic
from models.algorithm.minimax import Minimax
from models.board import Board
import random

class HeuristicTestMe(Heuristic):

  def heuristic(self, board, color):
    return random.randrange(-20, 20)

  def eval(self, old_value, new_value):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    return old_value > new_value # isso representa o max 

class HeuristicTestChallenger(Heuristic):

  def __init__(self, color):
    Heuristic.__init__(color)

  def heuristic(self, board, color):
    return random.randrange(-20, 20)

  def eval(self, old_value, new_value):
    #Lembre-se, uma heuristica tem que ser min, e o outro deve ser max
    return old_value < new_value # isso representa o min 

class TestPlayer(MinimaxPlayer):
  def __init__(self,color):
    MinimaxPlayer.__init__(color, 5, HeuristicTestMe(), HeuristicTestChallenger()):
