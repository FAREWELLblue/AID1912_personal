'''
    有两个线程，同时运行，一个线程要打印1--52这52个数字，另一个线程打印A--Z这26个字母
    通过互斥机制的控制让打印的结果为12A34B56C..5152Z
    提示：可能用多个同步互斥对象
'''
from threading import Thread, Lock

lock1=Lock()
lock2=Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()
def print_char():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1=Thread(target=print_num)
t2=Thread(target=print_char)
lock2.acquire()#让print_sum函数先打印
t1.start()
t2.start()
t1.join()
t2.join()