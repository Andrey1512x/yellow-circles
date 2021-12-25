import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.b = False
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        self.b = True
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw_circles()
        self.qp.end()

    def draw_circles(self):
        if self.b:
            self.b = False
            self.qp.setPen(QColor(0, 0, 0))
            self.qp.setBrush(QColor(255, 255, 0))
            for i in range(randint(6, 15)):
                x, y, r = randint(80, 320), randint(80, 520), randint(30, 80)
                self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
