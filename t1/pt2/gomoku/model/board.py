from gomoku.model.piece import Piece
from gomoku.model.position import Position

class Board(object):
  ROWS = 15
  COLUMNS = 15

  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.current_player = self.player1
    self.match_ended = False
    self.positions = []
    self.initialize_positions()

  def initialize_positions(self):
    for i in range(0, Board.ROWS):
      row = []
      for j in range(0, Board.COLUMNS):
        row.append(Position(i, j))
      self.positions.append(row)

  def analyze_move(self, move):
    if not self.match_ended:
      i, j = move
      position = self.positions[i][j]
      if position.is_empty():
        piece = Piece(self.current_player, position)
        position.set_piece(piece)
        self.switch_current_player()

  def switch_current_player(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1

  def check_victory_horizontal(self):
    for row in self.positions:
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for position in row:
        if not position.is_empty():
          player_in_current_position = position.get_player_from_position()
          if player_in_current_position == player_in_previous_position:
            i += 1
            if i == 5:
              self.match_ended = True
              return player_in_current_position
          else:
            i = 1
            player_in_previous_position = player_in_current_position
        else:
          i = 0

    return None

  def check_victory_vertical(self):
    for column in range(0, Board.ROWS):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for row in range(0, Board.COLUMNS):
        if not self.positions[row][column].is_empty():
          player_in_current_position = self.positions[row][column].get_player_from_position()
          if player_in_current_position == player_in_previous_position:
            i += 1
            if i == 5:
              self.match_ended = True
              return player_in_current_position
          else:
            i = 1
            player_in_previous_position = player_in_current_position
        else:
          i = 0

    return None

  def check_victory_diagonal_left_right(self):
    for k in range(-(Board.COLUMNS-1),1):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for row in range(0, Board.ROWS):
        if (row-k >= 0 and row-k < Board.COLUMNS):
          if not self.positions[row][row - k].is_empty():
            player_in_current_position = self.positions[row][row-k].get_player_from_position()
            if player_in_current_position == player_in_previous_position:
              i += 1
              if i == 5:
                self.match_ended = True
                return player_in_current_position
            else:
              i = 1
              player_in_previous_position = player_in_current_position
          else:
            i = 0
    for k in range(-(Board.COLUMNS-1),1):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for row in range(0, Board.ROWS):
        if (row-k >= 0 and row-k < Board.COLUMNS):
          if not self.positions[row-k][row].is_empty():
            player_in_current_position = self.positions[row-k][row].get_player_from_position()
            if player_in_current_position == player_in_previous_position:
              i += 1
              if i == 5:
                self.match_ended = True
                return player_in_current_position
            else:
              i = 1
              player_in_previous_position = player_in_current_position
          else:
            i = 0

  def check_victory_diagonal_right_left(self):
    for k in range(0, Board.ROWS):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for column in range(0, k+1):
        row = k - column
        if not self.positions[row][column].is_empty():
          player_in_current_position = self.positions[row][column].get_player_from_position()
          if player_in_current_position == player_in_previous_position:
            i += 1
            if i == 5:
              self.match_ended = True
              return player_in_current_position
          else:
            i = 1
            player_in_previous_position = player_in_current_position
        else:
          i = 0
    for k in range(Board.ROWS-2, -1,-1):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for column in range(0, k+1):
        row = k - column
        if not self.positions[Board.COLUMNS - column - 1][Board.ROWS - row -1].is_empty():
          player_in_current_position = self.positions[Board.COLUMNS - column - 1][Board.ROWS - row -1].get_player_from_position()
          if player_in_current_position == player_in_previous_position:
            i += 1
            if i == 5:
              self.match_ended = True
              return player_in_current_position
          else:
            i = 1
            player_in_previous_position = player_in_current_position
        else:
          i = 0
    return None

  def analyze_victory(self):
    horizontal_verical = self.check_victory_horizontal() or self.check_victory_vertical()
    diagonals = self.check_victory_diagonal_left_right() or self.check_victory_diagonal_right_left()
    return horizontal_verical or diagonals

  def restart_match(self):
    self.clear_positions()
    self.match_ended = False
    self.current_player = self.player1

  def clear_positions(self):
    for i in range(0, Board.ROWS):
      for j in range(0, Board.COLUMNS):
        self.positions[i][j].clear()

  def get_current_player(self):
    return self.current_player

  def get_match_ended(self):
    return self.match_ended

  def get_positions(self):
    return self.positions
