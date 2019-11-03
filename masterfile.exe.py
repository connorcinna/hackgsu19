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

qp = QPainter()

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

    def paintEvent(self, event): #This should be called whenever any drawing has to happen, or so it says -Brendon
        #qp = QPainter()
        #qp.begin(self)
        qp.begin(self)
        '''
        for i in range(32):
            self.drawRectangles(qp, x + (i*35), y*10) #y should vary with voltage of the read
        '''
        self.drawRectangles(qp, x=80, y=330)
        qp.end()

    def drawRectangles(self,qp, x, y):
        print(37)
        #qp = QPainter()
        qp.begin(self)
        col = QColor(0,0,0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(50,205,50))
        '''
        Draws 32 rectangles
        if the rectangle that you're trying to draw is the frequency index that is being passed in from serial
        then it erases that rectangle specifically and draws a new one with variable y value '''
        for i in range(32):
            qp.begin(self)
            qp.drawRect(x + (i*35), y, 30, 60) #y should vary with voltage of the read
            qp.end()
            if i == x:
                qp.eraseRect(x + (i*35), y, 30, 720)
                qp.drawRect(x + (i*35), y, 30, y*10)
        qp.end()
    def serial_in(self, qp):
        fft_buffer = []
        x = 80
        y = 330
        ser = serial.Serial(
        baudrate = 115200,
        port = '/dev/ttyACM0' #ports are /dev/ttyXXX on Linux, port are 'COMX' on windows
        )
        i = 0
        for i in range(100):
            reading_bytes_raw = ser.readline() #returns byte data type
            reading_str = str(reading_bytes_raw)
            reading_str = reading_str[2:len(reading_str)-5]
            if reading_str != '':
                reading_bytes = float(reading_str) #reading from arduino in bytes (float)
            else:
                continue
        reading_voltage = reading_bytes * 0.0049 #reading from arduino in volts
        fft_buffer.append(reading_voltage)
        ser.close()
        print(fft_buffer)
        fft_buffer = numpy.array(fft_buffer)
        f, t, sxx = signal.spectrogram(fft_buffer, 9600.0)
    #   lock.acquire()
        update_counters(f)
        qp.begin(self)
        qp.eraseRect(0,0,1280,720) #Clear All
        for count in counters:
            print('count: ' + str(count))
            self.drawRectangles(qp, x, count) #Brendon: If we just use drawRectangles, whats the point of creating a painterEvent when we just skip it.
        qp.end()
#    lock.release()

def update_counters(freqs):
    for i in freqs:
        if i > 50000:
            counters[31] += 1
        elif i > 40000:
            counters[30] += 1
        elif i > 30000:
            counters[29] += 1
        elif i > 20000:
            counters[28] += 1
        elif i > 10000:
            counters[27] += 1
        elif i > 9000:
            counters[26] += 1
        elif i > 8000:
            counters[25] += 1
        elif i > 7000:
            counters[24] += 1
        elif i > 6000:
            counters[23] += 1
        elif i > 5000:
            counters[22] += 1
        elif i > 4000:
            counters[21] += 1
        elif i > 3000:
            counters[20] += 1
        elif i > 2000:
            counters[19] += 1
        elif i > 1000:
            counters[18] += 1
        elif i > 900:
            counters[17] += 1
        elif i > 800:
            counters[16] += 1
        elif i > 700:
            counters[15] += 1
        elif i > 600:
            counters[14] += 1
        elif i > 500:
            counters[13] += 1
        elif i > 400:
            counters[12] += 1
        elif i > 300:
            counters[11] += 1
        elif i > 200:
            counters[10] += 1
        elif i > 100:
            counters[9] += 1
        elif i > 90:
            counters[8] += 1
        elif i > 80:
            counters[7] += 1
        elif i > 70:
            counters[6] += 1
        elif i > 60:
            counters[5] += 1
        elif i > 50:
            counters[4] += 1
        elif i > 40:
            counters[3] += 1
        elif i > 30:
            counters[2] += 1
        elif i > 20:
            counters[1] += 1
        else:
            counters[0] += 1

#lock = threading.Lock()
#t_serial = threading.Thread(target=serial_in, args=(lock,))
while 1:
    if __name__ == '__main__':
        counters = [0] * 32
        app = QApplication(sys.argv)
        print(157)
        ex = HackGSU() #Creating an instance of the class we just made
        ex.serial_in(qp) #Going ahed to start the class because serial_in should be theo nly thing to be called manually in main
 #       t_serial.start()
        #t_serial.join()
        print(160)
        app.exec_()
    