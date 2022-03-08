import socket
import json

ip = "127.0.0.1"
port = 12345
buffer_size = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(3)

while True:
    c, addr = s.accept()
    print("received from :",c)
    msg = c.recv(buffer_size).decode()
    new = json.loads(msg)
    print("the decoded json file object to json is:\n",new)