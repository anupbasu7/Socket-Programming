import socket

ip = '127.0.0.1'
port = 12345
buffer_size = 1024

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((ip,port))


msg = "E:/LT_Technology_Services/Network_Prog_Python/demo.txt"
msg = msg.encode()
client_sock.send(msg)
data = client_sock.recv(buffer_size)
data = data.decode()

print(data)
client_sock.close()