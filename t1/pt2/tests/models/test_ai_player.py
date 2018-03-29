import pytest

from gomoku.model import AIPlayer
from gomoku.model import Board
from gomoku.model import Player

@pytest.fixture(scope='session')
def ai_player():
  ai_player = AIPlayer('X')
  return ai_player

def test_get_symbol_for_ai(ai_player):
  assert ai_player.get_symbol() == 'X'

def test_calculate_points_diagonal(ai_player):
  player1 = Player('x')
  player2 = Player('o')
  board = Board(player1, player2)
  ai_player.calculate_points_diagonal(board, player1)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
