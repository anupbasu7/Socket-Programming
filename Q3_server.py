import socket
from datetime import datetime

ip = '127.0.0.1'
port = 12345
buffer_size = 4096

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))

data, client = sock.recvfrom(4096)

print(datetime.now(),data)
sock.sendto(b'Please connect',client)
sock.close()