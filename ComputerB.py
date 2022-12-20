import serial 

s = serial.Serial(port= None , baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
s.flushInput()  
data = s.read(16)
if data:
    print (data)
    s.flushOutput()
    s.write("*OKINI,COMPUTER_B*")
    s.flushInput()
    data2 = s.read(16)
    if data2:
        print (data2)
s.close()