import pytest

from gomoku.controller import GomokuController

@pytest.fixture(scope='session')
def gomoku_controller():
  gomoku_controller = GomokuController()
  return gomoku_controller

def test_analyze_move(gomoku_controller):
  winner = gomoku_controller.analyze_move((1,1))
  assert winner == None

def test_get_current_player_symbol(gomoku_controller):
  assert gomoku_controller.get_current_player_symbol() == 'O'

def test_restart_match(gomoku_controller):
  gomoku_controller.restart_match()
  assert gomoku_controller.get_current_player_symbol() == 'X'

def test_match_ended(gomoku_controller):
  assert gomoku_controller.match_ended() == False

def test_get_board(gomoku_controller):
  assert gomoku_controller.get_board() == gomoku_controller.board

def test_board_after_valid_move(gomoku_controller):
  gomoku_controller.analyze_move((1,1))
  assert gomoku_controller.get_board().get_positions()[1][1].get_player_from_position() == gomoku_controller.player1

if __name__ == '__main__':
  import doctest
  doctest.testmod()
