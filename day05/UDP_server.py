'''
    UDP_server.py
    重点代码
'''
from socket import *

ADDR=('127.0.0.1',8888)
# 创建UDP套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(ADDR)

# 循环收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    print('收到',addr,'消息：',data.decode())
    sockfd.sendto(b'Thanks',addr)

# 关闭套接字
sockfd.close()