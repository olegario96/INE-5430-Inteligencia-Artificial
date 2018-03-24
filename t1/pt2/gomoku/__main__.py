import sys
from PyQt5.QtWidgets import QApplication
from gomoku.view import MainWindow

def main(args):
  app = QApplication(args)
  mainWindow = MainWindow(args)
  sys.exit(app.exec_())

if __name__ == '__main__':
  args = list(sys.argv)
  main(args)
