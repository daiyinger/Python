from socket import *
import time


device_id = "131913"                        #设备ID
api_key = "cTwDAEzT3a7S8K5UUO78W93v170A"    #API_KEY
desc_id = "Speed"                           #数据点名称
values=0                                    #待传值

HOST = 'api.heclouds.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)



while True:
    values = values+1;
    Content = "{\"datastreams\":[{\"id\": \"temperature\",\"datapoints\": [{\"value\": "+str(values)+"}]},"
    Content +="{\"id\": \""+desc_id+"\",\"datapoints\": [{\"value\": "+str(values*2)+"}]}]}\r\n"
    value = len(Content)
    data = ''
    data +="POST /devices/"+device_id+"/datapoints HTTP/1.1\r\n"
    data +="Host:api.heclouds.com\r\n"
    data +="Connection: close\r\n"
    data +="api-key:"+api_key+"\r\n"
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
    time.sleep(5)
