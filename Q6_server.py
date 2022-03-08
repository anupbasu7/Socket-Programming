import socket
import json

port = 12345
ip = '127.0.0.1'
buffer_size = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((ip,port))
sock.listen(3)
print("socket is listening......")

while True:
    c, addr = sock.accept()
    print("connection got from",addr)

    jsonReceived = c.recv(buffer_size)

    print("Json objects decoded as:", jsonReceived)

    c.close()