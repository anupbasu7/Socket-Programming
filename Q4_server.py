import socket
import os
import os.path

ip = '127.0.0.1'
port = 12345
buffer_size = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)

c, addr = server.accept()
print('Connection address', addr)

msg = c.recv(buffer_size)
msg = msg.decode()
data = str(os.lstat(msg))
data = data.encode()

c.send(data)
c.close()
