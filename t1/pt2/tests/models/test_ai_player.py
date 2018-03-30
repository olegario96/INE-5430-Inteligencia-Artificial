import pytest

from gomoku.model import AIPlayer
from gomoku.model import Board
from gomoku.model import Player

@pytest.fixture(scope='session')
def ai_player():
  ai_player = AIPlayer('X')
  return ai_player

def test_simulate_move(ai_player):
  assert ai_player.simulate_move() == None

def test_minimax(ai_player):
  assert ai_player.minimax(None, 5) == None

def test_calculate_points_horizontal(ai_player):
  player2 = Player('O')
  board = Board(ai_player, player2)
  moves_for_horizontal_victory = [(1,1), (1,2), (1,3), (1,4), (1,5)]
  for move in moves_for_horizontal_victory:
    board.analyze_move(move)
    board.switch_current_player()
  ai_player.calculate_points_horizontal(board, ai_player)
  assert ai_player.sequences[4] == 1 and ai_player.gaps[4] == 2

def test_calculate_points_vertical(ai_player):
  player2 = Player('O')
  board = Board(ai_player, player2)
  moves_for_vertical_victory = [(1,1), (2,1), (3,1), (4,1), (5,1)]
  for move in moves_for_vertical_victory:
    print(board.get_current_player().get_symbol())
    board.analyze_move(move)
    print(board.get_current_player().get_symbol())
    board.switch_current_player()
    print(board.get_current_player().get_symbol())
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  print(board.get_current_player().get_symbol())
  ai_player.calculate_points_vertical(board, ai_player)
  assert ai_player.sequences[4] == 1 and ai_player.gaps[4] == 2

# def test_calculate_points_diagonal_left_right(ai_player):
#   player2 = Player('O')
#   board = Board(ai_player, player2)
#   moves_for_diagonal_victory = [(6,3), (7,4), (8,5), (9, 6), (10, 7)]
#   for move in moves_for_diagonal_victory:
#     board.analyze_move(move)
#     board.switch_current_player()
#   ai_player.calculate_points_diagonal_left_right(board, ai_player)
#   assert ai_player.sequences[4] == 1 and ai_player.gaps[4] == 2

# def test_calculate_points_diagonal_left_right_double(ai_player):
#   player2 = Player('O')
#   board = Board(ai_player, player2)
#   moves_for_diagonal_victory = [(1,3), (2,4), (3,5)]
#   for move in moves_for_diagonal_victory:
#     print(board.get_current_player().get_symbol())
#     board.analyze_move(move)
#     print(board.get_current_player().get_symbol())
#     board.switch_current_player()
#     print(board.get_current_player().get_symbol())
#     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#   print(board.get_current_player().get_symbol())
#   ai_player.calculate_points_diagonal_left_right(board, ai_player)
#   assert ai_player.sequences[2] == 1 and ai_player.gaps[2] == 2

# def test_calculate_points_diagonal_right_left(ai_player):
#   player2 = Player('O')
#   board = Board(ai_player, player2)
#   # DICA REESCREVER COMO SE FOSSE O ALGORITMO DE VERIFICAÇÃO DA ESQUERDA PRA DIREITA
#   # SÓ QUE MUDANDO O LAÇO MAIS INTERNO
#   moves_for_diagonal_victory = [(9,8), (8,7), (7,6), (6,5), (5,4)]
#   for move in moves_for_diagonal_victory:
#     board.analyze_move(move)
#     board.switch_current_player()
#   ai_player.calculate_points_diagonal_right_left(board, ai_player)
#   assert ai_player.sequences[4] == 1 and ai_player.gaps[4] == 2

if __name__ == '__main__':
  import doctest
  doctest.testmod()
