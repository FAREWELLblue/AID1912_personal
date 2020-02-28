'''
    要求：1.向一个文件中每隔两秒写入一行内容：
            1.2020-01-01 12：12:12
            2.2020-01-01 12：12:14
            3.2020-01-01 12：12:16
            4.2020-01-01 12：12:18
        2.打开文件随时可以看到已经写入的内容
        3.当程序终止以后，重新启动，继续写并且行号可以衔接
温馨提示：import time
    time.localtime()
    time.sleep()
    time.ctime()
'''
import time
f=open('time_play.txt','a+')
f.seek(0,0)
n=1
while f.readline():
    n+=1
while True:
    time.sleep(2)
    f.write(str(n)+'\t'+time.ctime()+'\n')
    f.flush()
    n+=1
