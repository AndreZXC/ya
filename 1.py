import sys
from PyQt5.QtWidgets import QWidget, QApplication
from ui import Ui_Form
from PyQt5.QtGui import QPainter, QColor
from random import randint


class WhatWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.XXX = False
        self.setupUi(self)
        self.spawnbtn.clicked.connect(self.spawn)

    def spawn(self):
        self.XXX = True
        self.repaint()

    def paintEvent(self, event):
        if self.XXX:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
            razm = randint(10, 200)
            qp.drawEllipse(randint(0, self.width() - razm), randint(0, self.height() - razm),
                           razm, razm)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WhatWindow()
    win.show()
    sys.exit(app.exec())