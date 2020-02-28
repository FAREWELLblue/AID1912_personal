'''
3.一个目录，在目录下有若干个文件（有子目录和普通文件）。编程将该目录下的普通文件复制到家目录下的'备份'文件夹中
 * 提前建立好这个备份文件夹
 * os.path.isfile（）判断普通文件与子目录

'''
import os

DIR = "/home/tarena/备份/"
dir = input(">>")
if dir[-1] != '/':
    dir += '/'

def copy(file):
    fr = open(dir+file,'rb')
    fw = open(DIR+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


def main():
    file_list = os.listdir(dir)
    for file in file_list:
        if os.path.isfile(dir+file):
            copy(file)

if __name__ == '__main__':
    main()