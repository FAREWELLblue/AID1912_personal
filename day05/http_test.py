from socket import *
s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
c,addr=s.accept()
data=c.recv(1024)

f=open('baidu.html')
data='''HTTP1.1 200 OK
Content-Type:text/html


'''+f.read()
c.send(data.encode())
c.close()
f.close()
s.close()