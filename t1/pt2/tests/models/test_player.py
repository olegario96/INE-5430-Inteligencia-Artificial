import pytest

from gomoku.model import Player

@pytest.fixture(scope='session')
def player():
  player = Player('X')
  return player

def test_player_initial_turn(player):
  assert not player.is_player_turn()

def test_get_symbol(player):
  assert player.get_symbol() == 'X'

def test_set_turn(player):
  player.switch_turn()
  assert player.is_player_turn()

def test_equality_operator(player):
  new_player = Player('O')
  assert not player == new_player

if __name__ == '__main__':
  import doctest
  doctest.testmod()
