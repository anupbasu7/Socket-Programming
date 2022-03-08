import socket

ip = "127.0.0.1"
port = 12345
buffer_size = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen()
print("Server is waiting for connection..")

c,a = s.accept()
print("Connection has been initialized from : ",a)
file = open("E:/LT_Technology_Services/Network_Prog_Python/demo.txt",'rb')
filedata = file.read(buffer_size)
c.send(filedata)
print("Data is sent successfully")