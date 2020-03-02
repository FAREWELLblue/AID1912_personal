'''
    模拟后端应用程序代码
>>从httpserver接收具体请求
>>根据请求进行逻辑处理和数据处理
>>将需要的数据反馈给httpserver


'''
from socket import *
import json
from threading import Thread
from settings import *  # 配置文件
from urls import *

ADDR = (frame_ip, frame_port)  # Wenframe地址


# 将功能封装成类
class Application:
    def __init__(self):
        self.address = ADDR
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        # TCP套接字 与浏览器通信
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 搭建并发服务
    def start(self):
        self.sockfd.listen(3)
        print('Listen the port %d' % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print('Connect from ', addr)
            t = Thread(target=self.handle, args=(connfd,))
            t.setDaemon(True)  # 主线程结束分支线程也结束
            t.start()

    # 处理来自httpserver的请求
    def handle(self, connfd):
        request = json.loads(connfd.recv(1024).decode())  # {"method": "GET", "info": "/sdsad"}
        # 分情况处理
        if request['method'] == 'GET':
            # 表示判定为一个网页
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html()
            else:  # 请求非网页内容
                response=self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass
        else:
            pass
        # 将数据给HTTPserver
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()


    # 处理网页
    def get_html(self, info):
        if info == '/':
            filename = dir + '/index.html'
        else:
            filename = dir + info

        try:
            f = open(filename)  # 尝试打开目标网页
        except:
            fd = open(dir + '/404.html')
            return {'status': '404', 'data': fd.read()}
        else:
            return {'status': '200', 'data': f.read()}

    # 处理非网页情形
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        return {'status':'404','data':'sorry..'}
app = Application()
app.start()
