class Player(object):
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol
    self.turn = False

  def is_player_turn(self):
    return self.turn

  def get_symbol(self):
    return self.player_symbol

  def switch_turn(self):
    if self.turn:
      self.turn = False
    else:
      self.turn = True

  def __eq__(self, other):
    return self.player_symbol == other.get_symbol()
