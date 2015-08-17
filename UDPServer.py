#!/usr/bin/env python
# UDP Echo Server -  udpserver.py
# code by www.cppblog.com/jerryma
import socket, traceback
import time

host = ''
port = 10006
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
while True:
        message, address = s.recvfrom(8192)
        print(message.decode())
        fp = open("logs.txt",'a')
        curTime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(time.time()))
        fp.write(curTime)
        fp.write(message.decode()+"\n");
        fp.close()
        #print ("Got data from", address, ": ", message)
        #s.sendto(message, address)