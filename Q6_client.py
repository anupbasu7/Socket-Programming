import socket
import sys
import json

object = {
  "Name": "Mini Cooper",
  "Category": "Car",
  "color": "black"
}
jsonResult = json.dumps(object).encode('utf-8')

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("socket error because of %s" %(err))
port = 12345
ip = '127.0.0.1'

try:
    s.connect((ip,port))
    s.send(jsonResult)
except socket.gaierror:
    print("error resolving the host")
    sys.exit()