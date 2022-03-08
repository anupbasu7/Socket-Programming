import socket

ip = "127.0.0.1"
port = 12345
buffer_size = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
print("Successfully connected!")

filename = input(str("please enter the filename: "))
file = open(filename,'wb')
filedata = s.recv(buffer_size)
file.write(filedata)
file.close()
print("File has been received")
s.close()