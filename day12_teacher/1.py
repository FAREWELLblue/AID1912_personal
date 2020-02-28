"""
httpserver 2.0
io多路服用，类封装练习
"""

from socket import *
from select import *
import os


# 具体功能实现
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.socketfd = socket()
        self.socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socketfd.bind((self.host, self.port))

    def start_server(self):
        """
            运行基于tcp的socket套接字
        Returns:
        """
        self.socketfd.listen(3)
        self.__run()

    def __run(self):
        p = epoll()
        p.register(self.socketfd, EPOLLIN)
        fdmap = {self.socketfd.fileno(): self.socketfd}
        while True:
            events = p.poll()
            print(events)
            for fileno, event in events:
                if fileno == self.socketfd.fileno():
                    c, addr = self.socketfd.accept()
                    c.setblocking(False)
                    p.register(c, EPOLLIN)
                    fdmap[c.fileno()] = c
                elif event & EPOLLIN:
                    c = fdmap[fileno]
                    data = c.recv(1024).decode()
                    #测试
                    print("***",data)
                    print("###")
                    if not data:
                        p.unregister(c)
                        c.close()
                        del fdmap[fileno]
                        continue
                    self.__request(c, data)



    def __request(self, connfd, data):
        """业务逻辑"""
        data = data.split(" ", 2)
        data = data[1]
        if data == "/":
            data = self.get_html_content(self.dir + "/index.html")
        elif os.path.exists(self.dir + data):
            data = self.get_html_content(self.dir + data)
        else:
            data = self.get_html_content(self.dir + "/error.html")
        self.__response(connfd, HTTPServer.org_response_str(data))

    @staticmethod
    def org_response_str(data):
        result = "HTTP/1.1 200 OK\r\n"
        result += "Content-Type:text/html\r\n"
        result += "\r\n"
        result += data
        return result

    def get_html_content(self, file):
        with open(file) as f:
            return f.read()

    def __response(self, connfd, data):
        if type(data) != bytes:
            data = data.encode()
        connfd.send(data)


if __name__ == '__main__':
    """
    希望通过使用这个类，可以快速搭建一个服务，展示我的网页
    """
    # 用户自己决定的内容
    HOST = '127.0.0.1'
    PORT = 8888
    DIR = "./static"
    # 实例化对象 --》 对象调用方法实现具体功能
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.start_server()  # 启动服务