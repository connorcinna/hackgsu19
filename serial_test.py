import serial
import time
import io 

ser = serial.Serial(
    baudrate = 115200,
    port = '/dev/ttyACM0' #ports are /dev/ttyXXX on Linux, port are 'COMX' on windows
)
'''
issue with this code is that the port we open is going to be platform dependent.
basically, we can only run this code on one machine. We should probably run it on my (Connor)
computer since it took me like 5 minutes to get the port working on linux opposed to
the over an hour I spent trying to get it to work on Michael's WSL. WSL apparenty has bugs
in some of the serial port programs for linux.

don't let me forget to turn michaels power settings back
'''
#ser.open()
ser.read(10)#reads 10 bytes from the serial input AKA the board

ser.close() 