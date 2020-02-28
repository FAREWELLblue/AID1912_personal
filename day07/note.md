## 孤儿和僵尸
1.孤儿进程：父进程先于子进程退出，此时子进程成为孤儿进程
> 特点：孤儿进程会被系统进程收养，此时系统进程就会成为孤儿进程新的父进程，孤儿进程退出该进程会自动处理。

2.僵尸进程：子进程先于父进程退出，父进程又没有处理子进程的退出状态，此时子进程就会被成为僵尸进程
> 特点：僵尸进程虽然结束，但是存留部分PCB在内存中，大量的僵尸进程会浪费系统的内存资源

3.如何避免僵尸进程产生
+ 使用wait函数处理子进程退出

pid,status=os.wait()
功能：在父进程中阻塞等待子进程退出
返回值：pid：退出的子进程的pid
       status：子进程退出状态
+ 创建二级进程处理僵尸
    【1】 父进程创建子进程，等待回收子进程
    【2】 子进程创建二级子进程然后退出
    【3】 二级子进程称为孤儿，和原来父进程一同执行事件
+ 通过信号处理子进程退出
> 原理：子进程退出时会发送信号给父进程，如果父进程忽略了子进程信号，则系统就会自动处理子进程退出
> 方法：使用signal模块在父进程创建子进程前写下语句：

import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
>特点：非阻塞，不会影响父进程进行，可以处理所有子进程退出


# 群聊聊天室
>功能 ： 类似qq群功能
【1】 有人进入聊天室需要输入姓名，姓名不能重复
【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx

思路：
    1.  需求分析 ---> 这个程序要达到什么效果（设计产品原型）
        结论：
    2.  技术分析 ---> 确定大概使用什么技术(概要设计，)
        聊天功能 ： 网络 ： UDP协议  （从服务端转发）
        服务端怎么存客户端地址：字典：{用户名：(ip,port)}
        客户端对消息的收发关系：多进程，发送和接收同时进行。一个负责接收，一个负责发送
    3. 结构设计 ---> 封装，使用什么模块，代码大体结构，功能分析，分为几个功能模块（封装，代码结构，功能分析）
        1 进入聊天室其他人会有通知
        2 聊天
        3 退出聊天室其他人会有通知
        代码架构模型：
            进入聊天室
            聊天
            退出聊天室
        模块：服务端 客户端
        封装：函数封装
    4. 通信协议设计 ---> 
        请求格式：请求类型（要让服务端干什么）   
                 请求参量（提供给服务端的信息）
                 进入聊天室： L name
                 聊天     ： C name content
                 退出聊天室： Q name
        回复格式：OK   成功
                FAIL 失败
    5. 代码分块实现并测试 --->
        代码架构模型：
        进入聊天室
            客户端
                1.输入姓名
                2.给服务端发送请求
                3.等待服务端反馈
                4.根据结果得到是否已经进入聊天室
            服务端
                1.接收请求
                2.判定客户端可否登录
                3.给客户端发送反馈
                4.给其他用户发送一个通知 并将其加入到user
        聊天
            客户端：
                创建两个进程一个发一个收
                1.创建子进程
                2.一个进程负责循环发送消息（输入->发送）
                3.一个进程负责循环接收消息（接收->打印）
            服务端：
                1.接收消息
                2.转发给其他人
        退出聊天室
            客户端：
                1.发送请求
                2.退出进程
                3.
            服务端：    
                1. 接收请求
                2. 告知其他人，并将该用户删除user

       