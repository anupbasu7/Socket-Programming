import socket
import json


ip = '127.0.0.1'
port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created..")
sock.bind((ip,port))
sock.listen(4)


while True:
    c, addr = sock.accept()
    print("connection got from",addr)

    jsonReceived = c.recv(1024)
    newjson = json.loads(jsonReceived)

    print("Received as dictionary:", newjson)

    c.close()