'''
基于thread的多进程并发
重点代码

步骤：
创建监听套接字
等待接收客户端请求
客户端连接创建新的线程处理客户端请求
原进程继续等待其他客户端连接
如果客户端退出，则对应分支线程退出

'''
from socket import socket
from threading import Thread

ADDR=('0.0.0.0',8888)
s=socket()
s.bind(ADDR)
s.listen(5)

def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

print('listen the port 8888')

#循环等待客户端连接
while True:
    c,addr=s.accept()
    print('Connect from', addr)
    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)#主线程退出时分支线程随之退出
    t.start()



