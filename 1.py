import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class WhatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.XXX = False
        uic.loadUi('Ui.ui', self)
        self.spawnbtn.clicked.connect(self.spawn)

    def spawn(self):
        self.XXX = True
        self.repaint()

    def paintEvent(self, event):
        if self.XXX:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            razm = randint(10, 200)
            qp.drawEllipse(randint(0, self.width() - razm), randint(0, self.height() - razm), razm, razm)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WhatWindow()
    win.show()
    sys.exit(app.exec())