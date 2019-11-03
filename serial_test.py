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
#from PyQt5.QtCore import Qt


class HackGSU(QtWidgets.QWidget):
    def serial(self):
        ser = serial.Serial(
        baudrate = 115200,
        port = '/dev/ttyACM0' #ports are /dev/ttyXXX on Linux, port are 'COMX' on windows
        )
        i = 0
        while True: #will continuously read data from serial port
            reading_bytes = ser.readline() #returns byte data type
            reading_str = str(reading_bytes)
            reading_str = reading_str[2:len(reading_str)-5]
            reading_float = float(reading_str)
            i += 1
        ser.close()

    def __init__(self):
        super(HackGSU,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('Music Visualizer')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        x = 40
        y = 330
        for i in range(40):
            self.drawRectangles(qp, x + (i*30), y)
        qp.end()

    def drawRectangles(self,qp, x, y):
        col = QColor(0,0,0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(x, y, 30, 60)

    def getData(self):
        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = HackGSU()
        sys.exit(app.exec_())
