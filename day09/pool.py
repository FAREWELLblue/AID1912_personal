'''
    进程池演示
    * 父进程结束，进程池销毁
    * 执行的事件函数必须在进程池创建之前声明
'''
from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

# 创建进程池
pool = Pool(4)

# 向进程池放事件
for i in range(10):
    msg= 'Tedu%d'%i
    pool.apply_async(func=worker,args=(msg,))
# 关闭进程池，无法再加入任务
pool.close()
# 等待进程结束
pool.join()