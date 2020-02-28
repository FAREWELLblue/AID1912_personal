'''
    tcp_server.py
    tcp服务端流程学习：重点代码
'''
import socket

# 1.创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定地址 ip:"localhost" "127.0.0.1" "0.0.0.0"

# 端口立即复用:程序结束后端口可以立即复用，要求在绑定之前
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

sockfd.bind(('127.0.0.1', 8888))
# 3.设置监听套接字
sockfd.listen(3)
# 4.处理客户端连接
while True:
    print('Waiting for connect....')
    connfd, addr = sockfd.accept()
    print('Connect from', addr)
    # 5.收发消息
    while True:
        data = connfd.recv(1024)# 在另外一端断开时会立刻返回一个空
        if not data:
            break
        print('Recv:', data.decode())
        n = connfd.send(b'Thanks')
        print(n)
    connfd.close()
sockfd.close()
