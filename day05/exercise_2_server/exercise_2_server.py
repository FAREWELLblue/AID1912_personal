'''
使用UDP完成
    从客户端输入一个小学生的信息
    包含 id  name  age  score
    将信息打包发送给服务端
    服务端收到信息之后如果成绩大于90，则将其信息写入一个文件中，每个学生信息写一行
'''
from socket import *
import struct

ADDR=('127.0.0.1',8888)
s= socket(AF_INET,SOCK_DGRAM)
s.bind(ADDR)
print('已开启服务端')
f = open('item.txt', 'a')
while True:
    data,addr=s.recvfrom(1024)
    info = struct.unpack('i10sii',data)
    print('接收到来自%s的内容'% addr,info)
    if info[3] >90:
        f.write('id:%d\tname:%s\tage:%d\tscore:%d\n'%(info[0],info[1].decode().strip('\x00'),info[2],info[3]))
    f.flush()
f.close()


