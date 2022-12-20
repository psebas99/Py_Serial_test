import serial 
import keyboard 
import time

ser = serial.Serial(port="COM1", baudrate=9600, bytesize=8, 
                    timeput=2, stopbits=serial.STOPBITS_ONE)

while True:
    ser.write("This is the message".encode('Ascii'))
    receive=ser.readline()
    print(receive.decode('Ascii'))
    #time.sleep(1)
    if keyboard.is_pressed('q'):
        print("User need to Quit the aplication")

