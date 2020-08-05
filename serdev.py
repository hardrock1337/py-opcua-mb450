import serial
import binascii
import time
import os

#TCP_IP = '194.120.111.254'
#TCP_PORT = 1337
#BUFFER_SIZE = 65535

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#s.send(messages)
#data = s.recv(BUFFER_SIZE)
#s.close()

s = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)
#s.open()
while True:
    mHex = s.read()
    if len(mHex) != 0:
        print("get", binascii.hexlify(bytearray(mHex)))
    #time.sleep(0.1)

#while True:

    #messages = s.readline()
    #messages = b"C0450064"
