'''
process 示例 创建多个子进程
'''

from multiprocessing import Process
import os
from time import sleep


def th1():
    sleep(3)
    print('吃饭')
    print(os.getppid(), '--', os.getpid())


def th2():
    sleep(2)
    print('睡觉')
    print(os.getppid(), '--', os.getpid())


def th3():
    sleep(4)
    print('打豆豆')
    print(os.getppid(), '--', os.getpid())


jobs = []
for th in (th1, th2, th3):
    p = Process(target=th)
    jobs.append(p)  # 保留进程对象
    p.start()
for i in jobs:
    i.join()
