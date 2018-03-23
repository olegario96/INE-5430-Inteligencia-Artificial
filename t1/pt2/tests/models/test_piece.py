import pytest

from gomoku.model import Piece
from gomoku.model import Player
from gomoku.model import Position
from random import randrange

@pytest.fixture(scope='session')
def piece():
  player = Player('X')
  position = Position(randrange(15), randrange(15))
  piece = Piece(player, position)
  return piece

def test_get_position(piece):
  assert piece.position == piece.get_position()

def test_get_player(piece):
  assert piece.player == piece.get_player()

if __name__ == '__main__':
  import doctest
  doctest.testmod()
