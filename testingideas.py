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
from PyQt5.QtCore import Qt
from serial_test import HackGSU
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QIcon, QColor, QGuiApplication
 
class HackGSU(QtWidgets.QWidget):
    
    def __init__(self):
        super(HackGSU,self).__init__()
        self.buildUI()
    def buildUI(self):
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('Music Visualizer')
        self.setStyleSheet("background-color: #333333;")
        
        self.show()
        print(26)

while 1:
    if __name__ == '__main__':
        counters = [0] * 32
        app = QApplication(sys.argv)
        print(157)
        ex = HackGSU()
        r0 = QRect(0, 10, 30, 60)
        r1 = QRect(1*35, 10, 30, 60)
        r2 = QRect(2*35, 10, 30, 60)
        r3 = QRect(3*35, 10, 30, 60)
        r4 = QRect(4*35, 10, 30, 60)
        r5 = QRect(5*35, 10, 30, 60)
        r6 = QRect(6*35, 10, 30, 60)
        r7 = QRect(7*35, 10, 30, 60)
        r8 = QRect(8*35, 10, 30, 60)
        r9 = QRect(9*35, 10, 30, 60)
        r10 = QRect(10*35, 10, 30, 60)
        r11 = QRect(11*35, 10, 30, 60)
        r12 = QRect(12*35, 10, 30, 60)
        r13 = QRect(13*35, 10, 30, 60)
        r14 = QRect(14*35, 10, 30, 60)
        r15 = QRect(15*35, 10, 30, 60)
        r16 = QRect(16*35, 10, 30, 60)
        r17 = QRect(17*35, 10, 30, 60)
        r18 = QRect(18*35, 10, 30, 60)
        r19 = QRect(19*35, 10, 30, 60)
        r20 = QRect(20*35, 10, 30, 60)
        r21 = QRect(21*35, 10, 30, 60)
        r22 = QRect(22*35, 10, 30, 60)
        r23 = QRect(23*35, 10, 30, 60)
        r24 = QRect(24*35, 10, 30, 60)
        r25 = QRect(25*35, 10, 30, 60)
        r26 = QRect(26*35, 10, 30, 60)
        r27 = QRect(27*35, 10, 30, 60)
        r28 = QRect(28*35, 10, 30, 60)
        r29 = QRect(29*35, 10, 30, 60)
        r30 = QRect(30*35, 10, 30, 60)
        r31 = QRect(31*35, 10, 30, 60)
        

 