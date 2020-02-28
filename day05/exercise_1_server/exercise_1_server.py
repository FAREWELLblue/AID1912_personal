'''
    使用udp套接字完成
    客户端循环输入单词，获取单词解释
    服务端负责接收单词，查询，将单词解释给客户端
'''
from socket import *

ADDR = ('127.0.0.1', 8888)


def find_word(word):
    f = open('dict.txt')
    for line in f:
        if line.split(' ')[0] == word:
            return line
        elif word < line.split(' ')[0]:
            return 'no this word'
    f.close()


s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)
while True:
    print('服务端开启，等待连接..')
    data,addr=s.recvfrom(1024)
    print('接收到',addr,'要查询的单词',data.decode())
    message=find_word(data.decode())
    s.sendto(message.encode(),addr)
s.close()

