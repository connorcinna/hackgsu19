import serial
import time
import io 
import matplotlib.pyplot as plt
import struct
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen 
from PyQt5.QtGui import QIcon, QColor

class HackGSU(QtWidgets.QWidget):
    def __init__(self):
        super(HackGSU,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('Music Visualizer')
        self.setStyleSheet("background-color: #333333;")
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        x = 80
        y = 330
        for i in range(32):
            self.drawRectangles(qp, x + (i*35), y)
        qp.end()

    def drawRectangles(self,qp, x, y):
        col = QColor(0,0,0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(50,205,50))
        qp.drawRect(x, y, 30, 60)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = HackGSU()
    sys.exit(app.exec_())
