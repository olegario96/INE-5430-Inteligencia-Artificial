from gomoku.model.piece import Piece
from gomoku.model.position import Position

class Board(object):
  ROWS = 15
  COLUMNS = 15

  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.current_player = self.player1
    self.player1.switch_turn()
    self.positions = []
    self.initialize_positions()

  def initialize_positions(self):
    for i in range(0, Board.ROWS):
      row = []
      for j in range(0, Board.COLUMNS):
        row.append(Position(i, j))
      self.positions.append(row)

  def analyze_move(self, move):
    if self.current_player.is_player_turn():
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
    self.player1.switch_turn()
    self.player2.switch_turn()

  def analyze_victory(self):
    self.check_victory_horizontal()
    self.check_victory_vertical()
    self.check_victory_diagonal_left_right()
    self.check_victory_diagonal_right_left()

  def check_victory_horizontal(self):
    for row in self.positions:
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for position in row:
        print(position)
        if not position.is_empty():
          player_in_current_position = position.get_player_from_position()
          if player_in_current_position == player_in_previous_position:
            print('oi')
            i += 1
            if i == 5:
              return player_in_current_position
          else:
            player_in_previous_position = player_in_current_position
            i = 1
        else:
          i = 0

    return None

  def check_victory_vertical(self):
    for row in range(0, Board.ROWS):
      i = 0
      player_in_previous_position = None
      player_in_current_position = None
      for column in range(0, Board.COLUMNS):
        player_in_current_position = self.positions[column][row].get_player_from_position()
        if player_in_current_position == player_in_previous_position:
          i += 1
          if i == 5:
            return player_in_current_position
        else:
          i = 0
          player_in_previous_position = player_in_current_position

    return None

  def check_victory_diagonal_left_right(self):
    pass

  def check_victory_diagonal_right_left(self):
    pass
