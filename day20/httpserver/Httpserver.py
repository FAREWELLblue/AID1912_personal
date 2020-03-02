'''
主程序代码

功能：
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
'''
from config import *
from socket import * #导入用户配置
from threading import Thread

# 服务器地址
ADDR=(HOST,PORT)


# 主题功能
class HTTPServer:
    def __init__(self):
        self.address =ADDR
        self.create_socket()
        self.bind()

   #创建套接字
    def create_socket(self):
        #TCP套接字
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    def bind(self):
        self.sockfd.bind(self.address)
        self.ip=self.address[0]
        self.port=self.address[1]

    # 搭建并发服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print('Listen the port %d'%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print('Connect from ',addr)
            t = Thread(target=self.handle,args=(connfd,))
            t.setDaemon(True)#主线程结束分支线程也结束
            t.start()
    # 具体处理浏览器请求
    def handle(self,connfd):
        request = connfd.recv(4096)
        print(request)

httpd = HTTPServer()
httpd.serve_forever() # 启动服务