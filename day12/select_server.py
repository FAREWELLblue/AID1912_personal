'''
select_server
重点代码
【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表，确定就绪IO事件
【4】处理发生的IO事件
'''
from socket import *
from select import select

# 创建监听套接字
s = socket()
s.bind(('127.0.0.0',8888))
s.listen(3)

s.setblocking(False)

# 设置关注列表
rlist=[s]# 处理客户端连接
wlist=[]
xlist=[]

while True:
    print('等待处理ＩＯ．．．．')
    rs,ws,xs=select(rlist,wlist,xlist)
    # 遍历返回值列表，看看哪个IO就绪了
    for r in rs:
        if r is s:
            c, addr = rs[0].accept()
            print('Connect from',addr)
            c.setblocking(True)
            rlist.append(c)# 将对应连接的套接字加入到关注列表
        else:
            # 如果遍历到客户端套接字，说明有客户端给我发消息
            data=r.recv(1024)
            if not data:
                # 如果客户端退出
                rlist.remove(r)# 将其从IO列表中删除
                continue
            print(data.decode())
            # r.send(b'OK')
            wlist.append(r)
    for w in ws:
        w.send(b'OK')
        wlist.remove(w)
    for x in xs:
        pass




