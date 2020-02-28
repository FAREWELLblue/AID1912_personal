'''
    编写一个函数，完成对文件的复制
    1.将file1复制一份，存为file2
        file1:传入你要复制的文件
        file2:传入你要将复制的文件存为什么
    思路：
        1.打开file1和file2
        2.从file1中读取出内容，将这些内容写入到file2中
        3.如果file1很大，应该循环的进行读写

'''
def copy(file1,file2):
    f1=open(file1,'rb')
    f2=open(file2,'wb')
    # f2.write(f1.read())
    # for line in f1:# 有的二进制文件没有按行读，可能整个文件只有一行，所以不能按行读或者写
    #     f2.write(line)
    while True:
        data=f1.read(1024)
        if not data:
            break
        f2.write(data)
    f1.close()
    f2.close()
copy('img/1_TCP.png','img/TCP.png')