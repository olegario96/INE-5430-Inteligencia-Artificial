import copy
import itertools
from math import inf
from gomoku.model import Board
from gomoku.model import Piece
from gomoku.model import Player

class AIPlayer(Player):
  MACHINE_STR = 'MACHINE'
  HUMAN_STR = 'HUMAN'
  global_alpha = float('-Inf')
  global_beta = float('Inf')

  def __init__(self, player_symbol):
    super(AIPlayer, self).__init__(player_symbol)
    self.sequences = [0,0,0,0,0]
    self.gaps = [0,0,0,0,0]
    self.started_with_gap = False
    self.ended_with_gap = False

  def simulate_move(self, board, player):
    best_pontuation = 0
    best_move = None
    copy_board = copy.deepcopy(board)
    positions = copy_board.get_positions()

    for row in positions:
      for position in row:
        if position.is_empty():
          piece = Piece(player, position)
          position.set_piece(piece)
          if player == self:
            pontuation = self.calculate_points_for_machine(copy_board)
          else:
            pontuation = self.calculate_points_for_human(copy_board)
          if pontuation > best_pontuation:
            best_pontuation = pontuation
            best_move = (position.get_row(), position.get_column())
          del piece
          position.set_piece(None)

    return best_move

  def minimax(self, board, human_player,level=5):
    if level == 0:
      return self.calculate_points(board, human_player)
    else:
      self.simulate_move(board, board.get_current_player())
      board.analyze_move(move)
      self.minimax(level-1)

  def calculate_points_horizontal(self, board, player):
    pieces_in_a_row = 0
    positions = board.get_positions()

    for i in range(0, Board.ROWS):
      for j in range(0, Board.COLUMNS):
        if not positions[i][j].is_empty() and positions[i][j].get_player_from_position() == player:
          pieces_in_a_row += 1
        else:
          if positions[i][j].is_empty() and pieces_in_a_row == 0:
            self.started_with_gap = True
          elif positions[i][j].is_empty() and pieces_in_a_row > 0:
            self.ended_with_gap = True
          elif not positions[i][j].is_empty() and pieces_in_a_row == 0:
            self.started_with_gap = False
          elif not positions[i][j].is_empty() and pieces_in_a_row > 0:
            self.ended_with_gap = False

          self.evaluate_pieces_in_a_row(pieces_in_a_row)
          pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False
      pieces_in_a_row = 0

  def calculate_points_vertical(self, board, player):
    pieces_in_a_row = 0
    positions = board.get_positions()

    for i in range(0, Board.ROWS):
      for j in range(0, Board.COLUMNS):
        if not positions[j][i].is_empty() and positions[j][i].get_player_from_position() == player:
          pieces_in_a_row += 1
        else:
          if positions[j][i].is_empty() and pieces_in_a_row == 0:
            self.started_with_gap = True
          elif positions[j][i].is_empty() and pieces_in_a_row > 0:
            self.ended_with_gap = True
          elif not positions[j][i].is_empty() and pieces_in_a_row == 0:
            self.started_with_gap = False
          elif not positions[j][i].is_empty() and pieces_in_a_row > 0:
            self.ended_with_gap = False

          self.evaluate_pieces_in_a_row(pieces_in_a_row)
          pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False
      pieces_in_a_row = 0

  def calculate_points_diagonal_left_right(self, board, player):
    positions = board.get_positions()
    pieces_in_a_row = 0

    for k in range(-(Board.COLUMNS-1),1):
      pieces_in_a_row = 0
      for row in range(0, Board.ROWS):
        if (row-k >= 0 and row-k < Board.COLUMNS):
          if not positions[row][row - k].is_empty():
            if positions[row][row - k].get_player_from_position() == player:
              pieces_in_a_row +=1
            else:
              if pieces_in_a_row == 0:
                self.started_with_gap = False
              else:
                self.ended_with_gap = False
              self.evaluate_pieces_in_a_row(pieces_in_a_row)
              pieces_in_a_row = 0
          else:
            if pieces_in_a_row == 0:
              self.started_with_gap = True
            else:
              self.ended_with_gap = True
            self.evaluate_pieces_in_a_row(pieces_in_a_row)
            pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False

    for k in range(-(Board.COLUMNS-1),1):
      pieces_in_a_row = 0
      for row in range(0, Board.ROWS):
        if (row-k >= 0 and row-k < Board.COLUMNS):
          if not positions[row-k][row].is_empty():
            if positions[row-k][row].get_player_from_position() == player:
              pieces_in_a_row += 1
            else:
              if pieces_in_a_row == 0:
                self.started_with_gap = False
              else:
                self.ended_with_gap = False
              self.evaluate_pieces_in_a_row(pieces_in_a_row)
              pieces_in_a_row = 0
          else:
            if pieces_in_a_row == 0:
              self.started_with_gap = True
            else:
              self.ended_with_gap = True
            self.evaluate_pieces_in_a_row(pieces_in_a_row)
            pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False

  def calculate_points_diagonal_right_left(self, board, player):
    positions = board.get_positions()
    pieces_in_a_row = 0

    for k in range(0, Board.ROWS):
      pieces_in_a_row = 0
      for column in range(0, k+1):
        row = k - column
        if not positions[row][column].is_empty():
          if positions[row][column].get_player_from_position() == player:
            pieces_in_a_row += 1
          else:
            if pieces_in_a_row == 0:
              self.started_with_gap = False
            else:
              self.ended_with_gap = False
            self.evaluate_pieces_in_a_row(pieces_in_a_row)
            pieces_in_a_row = 0
        else:
          if pieces_in_a_row == 0:
            self.started_with_gap = True
          else:
            self.ended_with_gap = True
          self.evaluate_pieces_in_a_row(pieces_in_a_row)
          pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False

    for k in range(Board.ROWS-2, -1,-1):
      pieces_in_a_row = 0
      for column in range(0, k+1):
        row = k - column
        if not positions[Board.COLUMNS - column - 1][Board.ROWS - row -1].is_empty():
          if positions[Board.COLUMNS - column - 1][Board.ROWS - row -1].get_player_from_position() == player:
            pieces_in_a_row += 1
          else:
            if pieces_in_a_row == 0:
              self.started_with_gap = False
            else:
              self.ended_with_gap = False
            self.evaluate_pieces_in_a_row(pieces_in_a_row)
            pieces_in_a_row = 0
        else:
          if pieces_in_a_row == 0:
            self.started_with_gap = True
          else:
            self.ended_with_gap = True
          self.evaluate_pieces_in_a_row(pieces_in_a_row)
          pieces_in_a_row = 0
      self.started_with_gap = False
      self.ended_with_gap = False

  def calculate_points(self):
    unary_sequences = 1 * self.sequences[0] * self.gaps[0]
    double_sequences = 60 * 1 * self.sequences[1]* self.gaps[1]
    triple_sequences = 150 * 60 * 1 * self.sequences[2]* self.gaps[2]
    quadruple_sequences = 89 * 150 * 60 * 1 * self.sequences[3]* self.gaps[3]
    quintuple_sequences = 62 * 89 * 150 * 60 * 1 * self.sequences[4]* self.gaps[4]
    self.restart_sequences_and_gaps()
    return unary_sequences + double_sequences + triple_sequences + quadruple_sequences + quintuple_sequences

  def restart_sequences_and_gaps(self):
    self.sequences = [0,0,0,0,0]
    self.gaps = [0,0,0,0,0]

  def calculate_value_for_move(self, board, human_player):
    return calculate_points_for_machine(board) - calculate_points_for_human(board, human_player)

  def calculate_points_for_machine(self, board):
    self.calculate_points_horizontal(board, self)
    self.calculate_points_vertical(board, self)
    self.calculate_points_diagonal_left_right(board, self)
    self.calculate_points_diagonal_right_left(board, self)
    return self.calculate_points()

  def calculate_points_for_human(self, board, human_player):
    self.calculate_points_horizontal(board, human_player)
    self.calculate_points_vertical(board, human_player)
    self.calculate_points_diagonal_left_right(board, human_player)
    self.calculate_points_diagonal_right_left(board, human_player)
    return self.calculate_points()

  def evaluate_pieces_in_a_row(self, pieces_in_a_row):
    if pieces_in_a_row == 0:
      return
    if pieces_in_a_row == 1:
      self.sequences[0] += 1
      if self.started_with_gap:
        self.gaps[0] += 1
      if self.ended_with_gap:
        self.gaps[0] += 1
    elif pieces_in_a_row == 2:
      self.sequences[1] += 1
      if self.started_with_gap:
        self.gaps[1] += 1
      if self.ended_with_gap:
        self.gaps[1] += 1
    elif pieces_in_a_row == 3:
      self.sequences[2] += 1
      if self.started_with_gap:
        self.gaps[2] += 1
      if self.ended_with_gap:
        self.gaps[2] += 1
    elif pieces_in_a_row == 4:
      self.sequences[3] += 1
      if self.started_with_gap:
        self.gaps[3] += 1
      if self.ended_with_gap:
        self.gaps[3] += 1
    elif pieces_in_a_row == 5:
      self.sequences[4] += 1
      if self.started_with_gap:
        self.gaps[4] += 1
      if self.ended_with_gap:
        self.gaps[4] += 1
