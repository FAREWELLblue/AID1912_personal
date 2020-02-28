'''
    获取100000以内的质数之和
    计算使用一个单进程程序执行该任务的用时
    再计算使用四个进程执行该任务用时
        思路：将100000分成4份，1--25000  25001--50000
    再计算使用10个进程执行该任务用时
        思路：将100000分成10份，1--10000  10001--20000
'''
import time
from multiprocessing import Process
def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print('函数执行时间：', end_time - start_time)
        return res

    return wrapper

# 判断一个数是不是质数
@timeit
def cacu(s, e):
    '''
        计算从s到e的所有质数，返回list
    :param s:开始值，int类型
    :param e:结束值，int类型

    '''
    list_result=[]
    for i in range(s, e + 1):
        for c in range(2, i):
            if i % c == 0:
                break
        else:
            list_result.append(i)
    print('%d--%d:'%(s,e),list_result)

# 一个进程
cacu(1,100000)
'''
# 四个进程
list_process = []
for i in range(4):
    p = Process(target=cacu, args=(25000 * i + 1, 25000 * (i + 1)))
    list_process.append(p)
    p.start()
for i in list_process:
    i.join()
print('-' * 50)

# 10个进程
list_process = []
for i in range(10):
    p = Process(target=cacu, args=(10000 * i + 1, 10000 * (i + 1)))
    list_process.append(p)
    p.start()
for i in list_process:
    i.join()
'''


# 判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
           return False
    return True



class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.begin=begin
        self.end=end
    def run(self):
        prime=[]
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))
# 四个进程
@timeit
def process_4():
    jobs=[]
    for i in range(1,100001,25000):
        p=Prime(i,i+25000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

# 十个进程
@timeit
def process_10():
    jobs=[]
    for i in range(1,100001,10000):
        p=Prime(i,i+10000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

