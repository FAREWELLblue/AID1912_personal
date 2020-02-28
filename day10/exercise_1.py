'''
作业：
使用多线程拷贝一个目录，要求同时拷贝该录下的这些文件
    比如：原目录--》os.listdir()（看有那些文件）
        os.mkdir()-->新目录
        创建10个线程，同事拷贝这些文件，将这些文件拷贝到新目录
思考思路：
1.拷贝文件怎么拷贝
2.查看一下目录中有多少文件，就创建多少线程
3.将文件从old_dir拷贝到new_dir
'''
import os
from threading import Thread

old_dir=input('要拷贝那个目录>>')
if old_dir[-1]=='/':
    old_dir=old_dir.rstrip('/')
new_dir=old_dir+'-备份'
print(new_dir)
try:
    file_list=os.listdir(old_dir)#文件列表
except:
    os._exit(0)
os.mkdir(new_dir)

def copy_file(file):
    print(old_dir+'/'+file)
    fr = open(old_dir+'/'+file,'rb')
    fw = open(new_dir+'/'+file,'wb')
    # 开始拷贝
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


# 根据文件多少创建线程
jobs=[]
for file in file_list:
    t=Thread(target=copy_file,args=(file,))
    t.start()
    jobs.append(t)
for i in jobs:
    i.join()