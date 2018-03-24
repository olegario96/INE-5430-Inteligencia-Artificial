from functools import partial
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

class MainWindow(QWidget):
  ROWS = 15
  COLUMNS = 15
  WIDTH = 550
  HEIGHT = 550

  def __init__(self, args):
    super(MainWindow, self).__init__()
    self.position_buttons = []
    self.restart_button = QPushButton('Restar match')
    self.current_player_label = QLabel()
    self.grid_layout = QGridLayout()
    self.init_components()
    self.setLayout(self.grid_layout)
    self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
    self.setWindowTitle('Gomoku')
    self.show()
    """
      TODO
    """
    self.gomoku_controller = None

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
    self.setFixedSize(200, 200)
    self.restart_button.clicked.connect(self.button_restart_clicked)
    self.grid_layout.addWidget(self.current_player_label, 15, 7, QtCore.Qt.AlignCenter)
    self.grid_layout.addWidget(self.restart_button, 16, 5, 16, 6)

  def button_position_clicked(self, i, j):
    print(i, j)

  def button_restart_clicked(self):
    """
      TODO
    """
    pass
