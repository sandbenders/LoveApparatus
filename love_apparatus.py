import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from loveApparatusInterface import Ui_MainWindow


class Window(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)

        # config the window
        self.setupUi(window)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = Window(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
