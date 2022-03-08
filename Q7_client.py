import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

add = input("Enter your device name/hostname:port -")
details = add.split(":")
print(details[0])

data = socket.gethostbyname(details[0])
print(data)