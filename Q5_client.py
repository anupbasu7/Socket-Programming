import socket
import sys
import json

jsonResult ={
    "emp1": {
        "name": "Bijoy",
        "designation": "Analyst",
        "age": "30",
        "salary": "60000"
    },
    "emp2": {
        "name": "Dev",
        "designation": "Software Developer",
        "age": "28",
        "salary": "90000"
    },
}
jsonResult = json.dumps(jsonResult).encode('utf-8')

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Socket error because of %s" %(err))
ip = '127.0.0.1'
port = 12345

try:
    s.connect((ip,port))
    s.send(jsonResult)
except socket.gaierror:
    print("There is an error resolving the host!")
    sys.exit()