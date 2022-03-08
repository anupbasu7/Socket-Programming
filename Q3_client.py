import socket
from datetime import datetime

ip = '127.0.0.1'
port = 12345
buffer_size = 4096

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_sock.sendto(b"Hey",(ip,port))

data, server = client_sock.recvfrom(buffer_size)
print(datetime.now(),data)
client_sock.close()