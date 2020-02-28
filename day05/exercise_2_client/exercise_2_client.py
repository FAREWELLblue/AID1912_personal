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
s=socket(AF_INET,SOCK_DGRAM)
while True:
    s.connect(ADDR)
    id = int(input('id:'))
    name = input('name:')
    age = int(input('age:'))
    score = int(input('score:'))
    data=struct.pack('i10sii',id,name.encode(),age,score)
    s.sendto(data,ADDR)
    if not input('>>'):
        break
s.close()