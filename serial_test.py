import serial
import time
import io 
import matplotlib.pyplot as plt
import struct
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen 
from PyQt5.QtCore import Qt

def gui():
    my_app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Music Visualizer')
    w.show()
    sys.exit(my_app.exec_())

def paintEvent(self, event):
    painter = QPainter(self)
    painter.setPen(QPen(Qt.red, 8, Qt.StraightLine))
    painter.drawRectangle(40,40,400,400)

ser = serial.Serial(
    baudrate = 115200,
    port = '/dev/ttyACM0' #ports are /dev/ttyXXX on Linux, port are 'COMX' on windows
)

i = 0
while True: #will continuously read data from serial port
    reading_bytes = ser.readline() #returns byte data type
    #print('reading_bytes: ' + str(reading_bytes))
    reading_str = str(reading_bytes)
    reading_str = reading_str[2:len(reading_str)-5]
    #print('reading_str: ' + reading_str)
    reading_float = float(reading_str)
    #print('reading_float: ' + str(reading_float))
    print(str(reading_float))
    #plt.scatter(i, reading_float) #cast reading to a float to plot it
    #plt.pause(0.005) # to allow the graph to update, dont know if this will throw off timing
    i += 1
#plt.show()

ser.close() 