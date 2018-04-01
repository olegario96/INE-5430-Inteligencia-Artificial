import itertools
from functools import partial
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from gomoku.controller import GomokuController

class MainWindow(QWidget):
  ROWS = 15
  COLUMNS = 15
  WIDTH = 550
  HEIGHT = 550

  def __init__(self, args):
    super(QWidget, self).__init__()
    self.position_buttons = []
    self.restart_button = QPushButton('Restart match')
    self.message_label = QLabel()
    self.grid_layout = QGridLayout()
    self.gomoku_controller = GomokuController()
    self.init_components()
    self.setLayout(self.grid_layout)
    self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
    self.setWindowTitle('Gomoku')
    self.show()

  def init_components(self):
    for i in range(0, MainWindow.ROWS):
      row = []
      for j in range(0, MainWindow.COLUMNS):
        button = QPushButton('')
        cbk = partial(self.button_position_clicked, i, j)
        button.clicked.connect(cbk)
        row.append(button)
        self.grid_layout.addWidget(button, i, j)
      self.position_buttons.append(row)
    self.restart_button.clicked.connect(self.button_restart_clicked)
    self.grid_layout.addWidget(self.message_label, 15, 5, 15, 8)
    self.update_label(None)
    self.grid_layout.addWidget(self.restart_button, 16, 5, 16, 6)

  def button_position_clicked(self, i, j):
    if not self.gomoku_controller.match_ended() and self.position_buttons[i][j].text() == '':
      move = (i, j)
      symbol = self.gomoku_controller.get_current_player_symbol()
      player = self.gomoku_controller.analyze_move(move)
      self.position_buttons[i][j].setText(symbol)
      self.update_label(player)
      QApplication.processEvents()
      self.ai_turn()

  def button_restart_clicked(self):
    self.gomoku_controller.restart_match()
    for row in self.position_buttons:
      for position in row:
        position.setText('')

  def update_label(self, player):
    if player == None:
      symbol = self.gomoku_controller.get_current_player_symbol()
      message = 'Player ' + symbol + ' turn'
    else:
      message = 'The winner player is ' + player.get_symbol()
    self.message_label.setText(message)

  def ai_turn(self):
    if not self.gomoku_controller.match_ended():
      self.gomoku_controller.move_for_ai()
      self.update_board()
      self.update_label(self.gomoku_controller.get_current_player())

  def update_board(self):
    for button_row, row in zip(self.position_buttons, self.gomoku_controller.get_board().get_positions()):
      for button, position in zip(button_row, row):
        if not position.is_empty():
          button.setText(position.get_player_from_position().get_symbol())

