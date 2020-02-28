'''
    UDP_client.py
    重点代码
'''
from socket import  *

ADDR=('127.0.0.1',8888)
# 创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    data=input('>>')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print(data.decode())
sockfd.close()