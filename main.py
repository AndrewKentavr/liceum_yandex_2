import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QBrush, QPen
import random
from PyQt5.QtCore import Qt
from interface import Ui_Dialog

class MyWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paintcircle)
        self.should_paint_circle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))

            num = random.randint(100, 450)
            x_and_y = 150 - (num / 4.3)
            painter.drawEllipse(x_and_y, x_and_y, num, num)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
