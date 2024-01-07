import serial
import time
import os

ser = serial.Serial('COM3', 9600)
def opros():
    while True:
        os.system('cls||clear')  
        mode = input("\non\noff\nservo\n:")
        if mode == "on":
            ser.write(b'1')
        elif mode == "off":
            ser.write(b'0')
        elif mode == "servo":
            ser.write(b'2')
        else:
            break            
try:
    opros()
except:
    print("Обшибка")
ser.close()
os.system('cls||clear')

