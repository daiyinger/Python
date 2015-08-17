from socket import *


HOST = '42.96.164.52'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
#Content="{\"value\":111,\"sensor_id\":\"33704\",\"device_id\":\"16877\"}\r\n"
Content="{\"value\":1}\r\n"

value = len(Content)

data = ''
data +="POST /v1.1/device/16877/sensor/31974/datapoints HTTP/1.1\r\n"
#data +="POST /v1.1/device/16877/sensor/33703/datapoints HTTP/1.1\r\n"
data +="Host:api.yeelink.net\r\n"
data +="Accept:*/*\r\n"
data +="U-ApiKey:9bedf55c4da4d3555218bffed9801080\r\n"
data +=("Content-Length:"+str(value)+"\r\n")
data +="Content-Type:application/x-www-form-urlencoded\r\n"
data +="Connection:close\r\n\r\n"
data +=Content

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

print (data)

while True:
    tcpCliSock.send(data.encode())
    print("after data send\n")
    data1 = tcpCliSock.recv(BUFSIZ).decode()
    if not data1:
        break
    print (data1)
    break
print("after while\n")
tcpCliSock.close()
