class Player(object):
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol

  def get_symbol(self):
    return self.player_symbol

  def __eq__(self, other):
    if other == None:
      return False
    else:
      return self.player_symbol == other.get_symbol()
