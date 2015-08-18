import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('localhost',8001))
while True:
    data,address = sock.recvfrom(1024)
    if not data:
        break
    sock.sendto(data,address)
sock.close()
