import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 20, 221, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гит и случайные окружности"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружности"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

            for i in range(randint(6, 15)):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                self.qp.setBrush(QColor(r, g, b))
                x, y, r = randint(80, 320), randint(80, 520), randint(30, 80)
                self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
