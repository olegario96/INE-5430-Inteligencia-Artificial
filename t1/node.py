import math.inf

class Node(object):
  MACHINE_STR = 'MACHINE'
  HUMAN_STR = 'HUMAN'
  global_alpha = float('-inf')
  global_beta = float('inf')

  def __init__(self, score, type_node):
    self.score = score
    self.type_node = type_node
    self.alpha = float('-inf')
    self.beta = float('inf')

  def minimax(level):
    if (level == 0):
      return self.score
    for neighbour in node.get_neighbours():
      score = neighbour.minimax(level-1)
      if self.type_node == MACHINE_STR:
        evaluate_alpha(score)
      else
        evaluate_beta(score)
    self.update_global_alpha_beta()


  def evaluate_alpha(score):
    if (score > self.alpha):
      self.alpha = score

  def evaluate_beta(self, score):
    if (score < self.beta):
      self.beta = score

  def update_global_alpha_beta(self):
    if self.type_node == MACHINE_STR:
      if self.alpha < global_beta:
        global_beta = self.alpha
    else
      if self.beta > global_alpha:
        global_alpha = self.beta
