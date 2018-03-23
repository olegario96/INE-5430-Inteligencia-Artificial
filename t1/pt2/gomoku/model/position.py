class Position(object):
  def __init__(self, i, j):
    super(Position, self).__init__()
    self.i = i
    self.j = j
    self.piece = None

  def is_empty(self):
    return self.piece == None

  def set_piece(self, piece):
    self.piece = piece

  def get_player_from_position(self):
    if self.piece != None:
      return self.piece.get_player()
    return None

  def get_row(self):
    return self.i

  def get_column(self):
    return self.j
