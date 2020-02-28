'''
    搭建一个http服务，当浏览器发起请求时向浏览器发送index.html文件

    * 将http处理部分分装为函数
    * 分析请求内容，如果请求内容是/则响应index.html网页
      如果请求内容是其他的则响应404
    * 重点代码
'''
from socket import *


# http 处理函数
def requeset():
    # http 请求获取
    data = c.recv(2048)
    # 防止客户端退出data等于空
    if not data:
        return
    data = data.decode()
    print(data)
    if data.split(' ')[1] == '/':
        f = open('index.html')
        data = '''HTTP/1.1 200 OK
Content-Type:text/html

''' + f.read()
        f.close()
    else:
        data = '''HTTP/1.1 404 NotFound
Content-Type:text/html

Sorry..Notfound
'''
    c.send(data.encode())
    c.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(('127.0.0.1', 20212))
s.listen(3)

# 等待客户端（浏览器）连接
while True:
    c, addr = s.accept()
    print('Connect from', addr)
    requeset()

s.close()
