import socket
import json
class employee:
    def __init__(self,account,employee,box,customer):
        self.account = account
        self.emp = employee
        self.box = box
        self.customer = customer

obj = employee('HDFC',99008066,'Developer','Anup')
Json = json.dumps(obj.__dict__)

ip = "127.0.0.1"
port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((ip,port))
sock.send(Json.encode())
sock.close()
