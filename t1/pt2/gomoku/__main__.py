import sys
from PyQt5.QtWidgets import QApplication

def main(args):
  app = QApplication(args)
  print('it worked!')
  sys.exit(app.exec_())

if __name__ == '__main__':
  args = list(sys.argv)
  main(args)
