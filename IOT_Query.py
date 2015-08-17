from socket import *
import time


HOST = 'api.heclouds.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
Content="{\"value\":1}\r\n"

value = len(Content)

data = ''
#data +="GET /devices?key_words=18:fe:34:9c:e3:38 HTTP/1.1\r\n"
data +="GET /devices/133838 HTTP/1.1\r\n"
data +="api-key:gHEjIJM3SDo8oPsII4MUysyGEAYA\r\n"
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
    print (data1)
    tcpCliSock.close()
    time.sleep(10)
