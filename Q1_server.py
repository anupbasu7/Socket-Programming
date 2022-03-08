import socket

ip = "127.0.0.1"
port = 12341
buffer_size = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((ip,port))
sock.listen(4)



while True:
    c, addr = sock.accept()
    msg = c.recv(buffer_size).decode()
    if msg =='squit':
        break
    msg = msg[::-1]
    c.send(msg.encode())

c.close()
sock.close()
