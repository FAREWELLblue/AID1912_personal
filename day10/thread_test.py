'''
线程效率测试
'''
import time
from multiprocessing import Process
from threading import Thread


def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


tm = time.time()
# 用时： 13.97511887550354
# for i in range(10):
#     count(1,1)
# 线程：用时： 13.204067945480347
# 进程：用时： 10.260632038116455
jobs = []
for i in range(10):
    t = Process(target=count, args=(1, 1))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
print('用时：', time.time() - tm)
