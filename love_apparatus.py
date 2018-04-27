import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

BACKGROUND_COLOR = Qt.black


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # config the window
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('#LoveApparatus')
        self.setCursor(Qt.BlankCursor)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), BACKGROUND_COLOR)
        self.setPalette(p)

        self.show()
        # self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
