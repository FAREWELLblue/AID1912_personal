'''
    使用udp套接字完成
    客户端循环输入单词，获取单词解释
    服务端负责接收单词，查询，将单词解释给客户端
'''
from socket import *

ADDR=('127.0.0.1',8888)
s= socket(AF_INET,SOCK_DGRAM)

while True:
    word=input(">>")
    if not word:
        break
    s.sendto(word.encode(),ADDR)
    data,addr=s.recvfrom(1024)
    print(data.decode())

s.close()