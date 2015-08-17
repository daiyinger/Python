from socket import *
import time


HOST = 'api.heclouds.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
values=0
#Content="{\"data\":{\"count\":1,\"datastreams\":[12]}}\r\n"








while True:
    values = values+1
    Content = "{\"datastreams\":[{\"id\": \"temperature\",\"datapoints\": [{\"value\": "+str(values)+"}]},"
    Content +="{\"id\": \"Speed\",\"datapoints\": [{\"value\": "+str(values*2)+"}]}]}\r\n"
    value = len(Content)
    data = ''
    data +="POST /devices/131913/datapoints HTTP/1.1\r\n"
    data +="Host:api.heclouds.com\r\n"
    data +="Connection: close\r\n"
    data +="api-key:cTwDAEzT3a7S8K5UUO78W93v170A\r\n"
    data +="Content-Length:"+str(value)+"\r\n"
    data +="\r\n"
    data +=Content
    
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send(data.encode())
    data1 = tcpCliSock.recv(BUFSIZ).decode()
    if not data1:
        break
    print (data1)
    tcpCliSock.close()
    time.sleep(0.1)
