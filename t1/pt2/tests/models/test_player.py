import pytest

from gomoku.model import Player

@pytest.fixture(scope='session')
def player():
  player = Player('X')
  return player

def test_get_symbol(player):
  assert player.get_symbol() == 'X'

def test_equality_operator(player):
  new_player = Player('O')
  assert not player == new_player

if __name__ == '__main__':
  import doctest
  doctest.testmod()
