import serial
import time
import io 
import matplotlib.pyplot as plt
import struct

ser = serial.Serial(
    baudrate = 115200,
    port = '/dev/ttyACM0' #ports are /dev/ttyXXX on Linux, port are 'COMX' on windows
)
'''
issue with this code is that the port we open is going to be platform dependent.
WSL has some strange issues regarding ports, so for now we're just going to run this on
Connor's computer.
'''
i = 0
while True: #will continuously read data from serial port
    reading_bytes = ser.readline() #returns byte data type
    print(reading_bytes)
    reading_int = int.from_bytes(reading_bytes, byteorder='big')
    print(str(reading_int))
    #print('reading_str: ' + reading_str)
    #reading_float = float(int(reading_str))
    #print('reading_float: ' + str(reading_float))
    #plt.scatter(i, reading_float) #cast reading to a float to plot it
    #plt.pause(0.05) # to allow the graph to update, dont know if this will throw off timing
    i += 1
#plt.show()
ser.close() 