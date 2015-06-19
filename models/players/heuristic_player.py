from models.heuristics.heuristic_test import *
from models.algorithm.minimax import MinimaxPlayer

class HeuristicPlayer(MinimaxPlayer):
  def __init__(self, color):
    MinimaxPlayer.__init__(color, 5, HeuristicTestMe(), HeuristicTestChallenger())
