'''
    thread线程函数传参
'''


# 含有参数的线程函数
from threading import Thread
from time import sleep


def func(sec,name):
    print('含有参数的线程')
    sleep(sec)
    print('%s执行完毕'%name)

# 创建多个线程
jobs=[]
for i in range(5):
    t = Thread(target=func,args=(2,),kwargs={'name':'T%d'%i})
    t.start()
    jobs.append(t)

for i in jobs:
    i.join()