class Piece(object):
  def __init__(self, player, position):
    self.player = player
    self.position = position

  def get_position(self):
    return self.position

  def get_player(self):
    return self.player

