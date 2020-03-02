'''
用于测试httpserver
'''
import json
from socket import *

s = socket()
s.bind(('0.0.0.0', 8080))
s.listen(3)
while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    print(data)
    d = {'status': '200', 'data': 'OK'}
    data = json.dumps(d)
    c.send(data.encode())
c.close()
s.close()
