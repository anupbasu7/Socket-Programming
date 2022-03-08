import socket

ip = "127.0.0.1"
port = 12341
buffer_size = 1024

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))

while True:
    msg = input("Type the message - ")
    if msg == 'cquit':
        break
    client.send(msg.encode())
    msg = client.recv(buffer_size)
    print("Echo server: ",msg.decode())
    

client.close()