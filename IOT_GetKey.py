from socket import *
import time


HOST = 'api.heclouds.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
Content="{\"value\":1}\r\n"

value = len(Content)

data = ''
data +="GET /devices/131913/datapoints?datastream_id=Speed HTTP/1.1\r\n"
data +="api-key:cTwDAEzT3a7S8K5UUO78W93v170A\r\n"
data +="Connection: close\r\n"
data +="Host:api.heclouds.com\r\n"
data +="\r\n"


databak = 0

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send(data.encode())
    data1 = tcpCliSock.recv(BUFSIZ).decode()
    if not data1:
        break
    #print (data1)
    datai = int(data1[data1.find("\"value\":")+8:data1.find("\"id\":")-3])
    if databak != datai:
        print(datai)
    databak = datai
    tcpCliSock.close()
    time.sleep(0.1)
