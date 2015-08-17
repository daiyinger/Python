from socket import *
import time


HOST = '42.96.164.52'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
Content="{\"value\":1}\r\n"

value = len(Content)

data = ''
data +="GET /v1.1/device/16993/sensor/33703/datapoints HTTP/1.1\r\n"
data +="Host:api.yeelink.net\r\n"
data +="Accept:*/*\r\n"
data +="U-ApiKey:9bedf55c4da4d3555218bffed9801080\r\n"
#data +=("Content-Length:"+str(value)+"\r\n")
data +="Content-Type:application/x-www-form-urlencoded\r\n"
data +="Connection:close\r\n\r\n"
#data +=Content


while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send(data.encode())
    data1 = tcpCliSock.recv(BUFSIZ).decode()
    if not data1:
        break
    print (data1)
    tcpCliSock.close()
    time.sleep(5)
