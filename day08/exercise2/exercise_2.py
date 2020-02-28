'''
2.文件分离：
一个文件，文件名：'talk.txt'，在文件保存着一些对话信息，格式如下：
       老王：   吃了么
       老李：   没那，您呢？
    ​   老张:   您二位干什么呢
    ​   老李:   遛弯啊，刚买菜回来啊
    ​   老张：   是啊
通过程序将文件进行分离，每个人物的说话内容，重新写入到一个新的文件中，文件以这个人的名字命名
'''
f=open('talk.txt','r')
for line in f:
    name=line.split('：',1)[0]
    with open(name+'.txt','a') as fw:
        fw.write(line.split('：',1)[1].strip(' '))
    print(name)