'''
    TCP_clinet.py
    tcp客户端演示：重要代码
'''
from socket import *

# 声明服务器地址
server_addr=('127.0.0.1',8888)
# 创建套接字
sockf=socket()# 默认IPv4 流式套接字
# 连接服务器
sockf.connect(server_addr)
# 发送接收消息
while True:
    data = input(">>")
    if not data:
        break
    sockf.send(data.encode())
    # 输入##表示退出
    # if data == '##':
    #     break
    data = sockf.recv(1024)
    print("From server:",data.decode())
