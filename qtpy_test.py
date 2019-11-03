import io
import numpy
import threading
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from serial_test import HackGSU

line = ''
'''
def gui(lock):
    my_app = QApplication(sys.argv)
    w=QWidget()
    w.setWindowTitle('Visualization')
    w.show()
    sys.exit(my_app.exec_())
    '''
ex = HackGSU()
def calculation(lock):
    print(line)
    line = float(line)
    volt = line * .0049

# read data from file (board doesn't work with this computer)
mic_data = open("output.txt",'r')
lock = threading.Lock()
t1 = threading.Thread(target=ex.initUI)
t2 = threading.Thread(target=calculation, args=(lock,))

# start threads
t1.start()
t2.start()

# pull in microphone data and convert to float, then convert to frequency data
for line in mic_data:
    t2.join()
    t1.join()

 # close data file
mic_data.close()