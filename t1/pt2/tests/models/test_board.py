import copy
import pytest

from gomoku.model import Board
from gomoku.model import Player
from random import randrange

@pytest.fixture(scope='module')
def board():
  player1 = Player('X')
  player2 = Player('O')
  board = Board(player1, player2)
  return board

def test_initialize_positions(board):
  assert len(board.positions) == 15 and len(board.positions[randrange(15)])

def test_turn_for_current_player(board):
  assert board.current_player.is_player_turn()

def test_not_player2_turn(board):
  assert not board.player2.is_player_turn()

def test_get_current_player(board):
  assert board.get_current_player() == board.player1

def test_match_not_ended(board):
  assert not board.match_ended

def test_switch_current_player(board):
  board.switch_current_player()
  assert board.player2.is_player_turn()

def test_analyze_move(board):
  move = (14, 14)
  i, j = move
  board.analyze_move(move)
  switch_player = board.player2.is_player_turn() == False
  position_not_empty = board.positions[i][j].is_empty() == False
  assert position_not_empty and switch_player

def test_check_victory_horizontal(board):
  copy_board = copy.deepcopy(board)
  moves_for_horizontal_victory = [(1,1), (1,2), (1,3), (1,4), (1,5)]
  for move in moves_for_horizontal_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.check_victory_horizontal() == board.player1

def test_check_victory_vertical(board):
  moves_for_vertical_victory = [(1,6), (2,6), (3,6), (4,6), (5,6)]
  for move in moves_for_vertical_victory:
    board.analyze_move(move)
    board.switch_current_player()
  assert board.check_victory_vertical() == board.player1

def test_get_match_ended(board):
  assert board.get_match_ended()

def test_clear_positions(board):
  board.clear_positions()
  assert board.positions[randrange(15)][randrange(15)].is_empty()

def restart_match(board):
  board.restart_match()
  assert board.get_current_player() == board.player1

if __name__ == '__main__':
  import doctest
  doctest.testmod()
