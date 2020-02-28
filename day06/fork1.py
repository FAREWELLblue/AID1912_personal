'''
    fork进程的演示示例
'''
import os
from time import sleep

print('-----------------------')
a=1

# 创建进程
pid = os.fork()

if pid<0:
    print('进程创建失败')
elif pid==0:
    print(a)
    a=1000
    print('新的进程')
else:
    sleep(0.5)
    print(a)
    print('原来的进程')
print(a)