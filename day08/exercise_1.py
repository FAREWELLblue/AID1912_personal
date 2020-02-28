'''
  利用多进程完成文件拆分
  有一个文件比较大，要拆分成两个，按照字节大小平均分
  一个进程拷贝上半部分，与此同时，另一个进程拷贝下半部分
  * os.path.getsize()获取文件大小
  * seek（）偏移量
'''
import os

filename='dict.txt'
size=os.path.getsize(filename)

# 复制上半部分
def top():
    fr= open(filename, 'rb')
    fw = open('dict2.txt', 'rb+')
    point=size//2
    print(point)
    fw.write(fr.read(point))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('dict2.txt', 'rb+')
    point = size // 2
    print(point)
    fw.seek(point,0)
    fr.seek(point,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

pid=os.fork()
if pid<0:
    print('error')
elif pid==0:
    top()
    print('上半部分复制完成')
else:
    bot()
    print('下半部分复制完成')
