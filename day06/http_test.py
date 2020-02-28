'''
    http基本演示
'''
from socket import *
s=socket()
s.bind(('127.0.0.1',8000))
s.listen(3)

# 等待客户端（浏览器）连接
c,addr=s.accept()
print('Connect from',addr)

# http 请求获取
data=c.recv(2048)
print(data.decode())

# 发送简单数据
# c.send(b'hello world')
#   发送的响应无效

# data='''HTTP/1.1 200 OK
# Content-Type:text/html
#
# Hello World
# '''

data="HTTP/1.1 200 OK\r\n"
data+='Content-Type:text/html\r\n'
data+='\r\n'
data+='hello World'

c.send(data.encode())

c.close()
s.close()