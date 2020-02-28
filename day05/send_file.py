'''
上传头像  将一个图片从客户端发送给服务端
思路：客户端 读取头像图片内容 --》通过网络发送给服务端
     服务端 先从网络中接收内容--》写入到服务端的文件
'''
from socket import *
import time

ADDR = ('127.0.0.1', 8888)
# 创建套接字
s = socket()
# 发起连接
s.connect(ADDR)
# 发送文件
f=open('TCP.png','rb')
while True:
    data=f.read(1024)
    if not data:
        time.sleep(1)
        s.send('文件发送完毕'.encode())
        break
    s.send(data)

f.close()
s.close()