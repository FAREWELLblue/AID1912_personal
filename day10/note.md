# 线程间通信方法
## 1.通信办法
> 线程间使用全局变量通信
## 2.共享资源争夺
+ 共享资源：多个进程或多个线程都可以操作的资源成为龚爱那个资源。对共享资源的操作代码成为临界区
+ 影响：对共享资源的无序操作可能会带来数据的混乱，或者操作错误。此时往往需要同步互斥机制协调操作顺序。
## 3.同步互斥机制
# 线程同步互斥方法
## 线程Event
```python	
from threading import Event
e=Event()创建线程event对象
e.wait([timeout])阻塞等待e被set
e.set()设置e，是wait结束阻塞
e.clear()使e回到未被设置状态
e.is_set()查看当前e是否被设置状态
```
## 线程锁
```
from threading import Lock
lock=Lock()创建锁对象
lock.acquire()上锁，如果lock已经上锁则会阻塞
lock.release()解锁
with lock:上锁
语句块，结束后自动解锁
```
##死锁
///
# python 线程GIL
**所以python多线程在执行多阻塞高延迟IO时可以提升程序效率，其他情况并不能对效率有所提升**
# 进程和线程
## 区别联系
1. 两者都是多任务编程方式，都能使用计算机多核资源
2. 进程的创建删除消耗的计算机资源比线程多
3. 进程空间独立，数据互不干扰，有专门通信方法。线程使用全局变量通信
4. 一个进程可以有多个分支线程，两者有包含关系
5. 多个线程共享进程资源，在共享资源操作时往往需要同步互斥处理
6. 进程线程在系统中都有自己的特有属性标志，如id，代码段，命令集等
## 使用场景
1. 任务场景：如果是相对独立的任务模块，可能使用多进程，如果是多个分支共同形成一个整体任务可能用多线程
2. 项目结构：多种编程语言实现不同任务模块，可能是多进程，或者前后端分离应该各自为一个进程
3. 难以程度：通信难度，数据处理的复杂度来判断用进程间通信还是同步互斥法
## 面试要求
1. 对进程线程怎么理解/说说进程线程的差异
2. 进程间通信知道哪些，有什么特点
3. 什么是同步互斥，你什么情况下使用，怎么用
4. 给一个情形，说说用进程还是线程，为什么
5. 问一些概念，僵尸进程的处理，GIL问题，进程状态
# 常见网络模型

#作业：
1、并发模型自己会写
2、尝试ftp文件服务器