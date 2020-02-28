'''
基于fork的多进程并发
重点代码

步骤：
创建监听套接字
等待接收客户端请求
客户端连接创建新的进程处理客户端请求
原进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程

'''
import signal
from socket import *
import os

#全局变量
HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)

# 创建监听套接字
s=socket()
s.bind(ADDR)
s.listen(3)

def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

print('listen the port 8888')
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#循环等待客户端连接
while True:
    c,addr=s.accept()
    print('Connect from',addr)

    #创建一个新的进程处理客户端请求
    pid = os.fork()
    if pid==0:
        # 处理客户端请求
        handle(c)# 处理客户端请求
        os._exit(0)# 子进程处理完客户端请求后就退出
    else:
        # 出错或者父进程都继续等待客户端连接
        continue
