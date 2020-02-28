'''
上传头像  将一个图片从客户端发送给服务端
思路：客户端 读取头像图片内容 --》通过网络发送给服务端
     服务端 先从网络中接收内容--》写入到服务端的文件
'''
from socket import *

# 创建监听套接字
s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(5)

# 等待客户端连接
c, addr = s.accept()
print('Connect from', addr)

# 接收图片
f = open('gg.jpg', 'wb')

# 循环接收，因为图片或文件不一定能一次全部接收完
while True:
    data = c.recv(1024)# 如果客户端退出，recv会返回空
    # if data.decode()=='文件发送完毕':
        # 因为这样每次接收都会尝试decode，文件二进制是不能decode的
    if data=='文件发送完毕'.encode():
        print('接收完成')
        break
    f.write(data)

f.close()
c.close()
s.close()