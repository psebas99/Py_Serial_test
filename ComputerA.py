import serial 

s = serial.Serial(port= None, baudrate=19200, bytesize=8, parity='N', stopbits=serial.STOPBITS_ONE , timeout=None, xonxoff=0, rtscts=0)
s.flushOutput()
s.write("*INI,COMPUTER_A*")
s.flushInput()  
data = s.read(16)
if data:
    print (data)
    s.flushOutput()
    s.write("*OK,COMPUTER_A*")
s.close()