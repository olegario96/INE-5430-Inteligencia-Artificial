from gomoku.model import Board
from gomoku.model import Player
from gomoku.model import AIPlayer

class GomokuController(object):
  def __init__(self):
    self.player1 = Player('X')
    self.player2 = AIPlayer('O')
    self.board = Board(self.player1, self.player2)

  def analyze_move(self, move):
    self.board.analyze_move(move)
    return self.board.analyze_victory()

  def get_current_player_symbol(self):
    return self.board.get_current_player().get_symbol()

  def get_current_player(self):
    return self.board.get_current_player()

  def restart_match(self):
    self.board.restart_match()

  def match_ended(self):
    return self.board.get_match_ended()

  def move_for_ai(self):
    self.board.check_move((1,1))
    move = self.player2.minimax(self.board, self.player1, self.player2.global_alpha, self.player2.global_beta)
    self.board.remove_last_move(self.board.last_move_for_ai)
    self.analyze_move(move[1])

  def get_board(self):
    return self.board
