from gomoku.model.board import Board
from gomoku.model.player import Player

class GomokuController(object):
  def __init__(self):
    self.player1 = Player('X')
    self.player2 = Player('O')
    self.board = Board(self.player1, self.player2)

  def analyze_move(self, move):
    self.board.analyze_move(move)
    return self.board.analyze_victory()

  def get_current_player_symbol(self):
    return self.board.get_current_player().get_symbol()

  def restart_match(self):
    self.board.restart_match()

  def match_ended(self):
    return self.board.get_match_ended()

  def get_board(self):
    return self.board
