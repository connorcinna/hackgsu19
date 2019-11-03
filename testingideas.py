import serial
import datetime 
import io 
from scipy import signal
import matplotlib.pyplot as plt
import struct
import sys
import numpy
import threading
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRect
from serial_test import HackGSU
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QIcon, QColor, QGuiApplication, QPaintDevice
 

k = 0
qp = QPainter()
class HackGSU(QtWidgets.QWidget):
    def __init__(self):
        super(HackGSU,self).__init__()
        self.buildUI()
        self.buildRect()
    def buildUI(self):
        qd = QPaintDevice()
        self.QPaintDevice()
        self.show()
        print(26)

    def QPaintDevice(self):
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('Music Visualizer')
        self.setStyleSheet("background-color: #333333;")

    def paintEvent(self, event): #This should be called whenever any drawing has to happen, or so it says -Brendon
        qp = QPainter(self)
        self.drawRect(qp, k)

    def drawRect(self, qp, x):
        qp.begin(self,QPaintDevice)
        qp.setPen(QColor(50,205,50))
        qp.setBrush(QColor(50, 205, 50))
        qp.drawRect(35 + (k * 35), 300, 30, 60)
        qp.end()
        

    def buildRect(self):
        r = [None] * 32
        for k in range(32):
            r[k] = (self.paintEvent(self.drawRect(qp, k * 35)))  
    

while 1:
    if __name__ == '__main__':
        counters = [0] * 32
        app = QApplication(sys.argv)
        print(157)
        k = 0
        ex = HackGSU()
        ex.show()
        app.exec()


 