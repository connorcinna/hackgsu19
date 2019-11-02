import io
import time
import struct 
import numpy
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen 
from PyQt5.QtCore import Qt

def gui(title):
    my_app = QApplication(sys.argv)
    w=QWidget()
    w.setWindowTitle(title)
    w.show()
    sys.exit(my_app.exec_())

def calculation():
    # read data from file (board doesn't work with this computer)
    mic_data = open("output.txt",'r')

    for line in mic_data:
        print(line)
        line = float(line)

    
    # close data file
    mic_data.close()



class my_thread (threading.Thread):
    def __init__(self,thread_ID,name,purpose):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.name = name
        self.purpose = purpose
    
    def run(self):
        print('Starting ' + self.name)
        print('Thread purpose: ' + self.purpose)
        if(purpose == 'calculation'):
            calculation()
        elif(purpose == 'gui'):
            gui('Visualization')
        else:
            print('Invalid thread type')
    
    def 


