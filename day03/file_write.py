'''
    file_write.py
    文件的写操作
'''
f=open('file','w')
# f.write('hello,world\n')
# f.write('hello,cat')
str_list=['你好','hello','hi']
f.writelines(str_list)
f.close()
'''
    with 生成对象的语句 as 生成对象的对象名：
        生成对象的对象名的作用域 
'''
