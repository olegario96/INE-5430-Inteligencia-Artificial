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

def test_analyze_move(board):
  move = (randrange(15), randrange(15))
  i, j = move
  board.analyze_move(move)
  switch_player = board.player2.is_player_turn() == True
  position_not_empty = board.positions[i][j].is_empty() == False
  assert position_not_empty and switch_player

def test_switch_current_player(board):
  board.switch_current_player()
  assert board.player1.is_player_turn()

def test_check_victory_horizontal(board):
  copy_board = copy.deepcopy(board)
  moves_for_horizontal_victory = [(1,1), (1,2), (1,3), (1,4), (1,5)]
  for move in moves_for_horizontal_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.check_victory_horizontal() == copy_board.player1

def test_check_victory_vertical(board):
  copy_board = copy.deepcopy(board)
  moves_for_vertical_victory = [(1,6), (2,6), (3,6), (4,6), (5,6)]
  for move in moves_for_vertical_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.check_victory_vertical() == copy_board.player1

def test_check_victory_diagonal_left_right(board):
  copy_board = copy.deepcopy(board)
  moves_for_diagonal_left_right_victory = [(1,1), (2,2), (3,3), (4,4), (5,5)]
  for move in moves_for_diagonal_left_right_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.check_victory_diagonal_left_right() == copy_board.player1

def test_check_victory_diagonal_right_left(board):
  copy_board = copy.deepcopy(board)
  moves_for_diagonal_right_left_victory = [(7,7), (6,8), (5,9), (4,10), (3,11)]
  for move in moves_for_diagonal_right_left_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.check_victory_diagonal_right_left() == copy_board.player1

def test_analyze_victory(board):
  copy_board = copy.deepcopy(board)
  moves_for_diagonal_right_left_victory = [(7,7), (6,8), (5,9), (4,10), (3,11)]
  for move in moves_for_diagonal_right_left_victory:
    copy_board.analyze_move(move)
    copy_board.switch_current_player()
  assert copy_board.analyze_victory() == copy_board.player1

def restart_match(board):
  board.restart_match()
  assert board.get_current_player() == board.player1

def test_clear_positions(board):
  board.clear_positions()
  assert board.positions[randrange(15)][randrange(15)].is_empty()

def test_get_current_player(board):
  assert board.get_current_player() == board.player1

def test_get_match_ended(board):
  assert board.get_match_ended() == False

def test_get_positions(board):
  assert board.get_positions() == board.positions

def test_turn_for_current_player(board):
  assert board.get_current_player().is_player_turn()

# FAZER UM TESTE JOGANDO UMA PEÇA NUM LUGAR QUE JÁ TEM UMA
# TESTAR FINAL DA PARTIDA PARA UM TABULEIRO QUE TERMINOU

if __name__ == '__main__':
  import doctest
  doctest.testmod()
