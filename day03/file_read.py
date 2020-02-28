'''
    练习：使用dict.txt文件完成单词的查找
    1.使用input输入一个单词
    2.查找到这个单词，打印出该单词及其解释

    温馨提示：每个单词占一行，单词与解释之间有空格，按照从小到大的顺序排列

'''
word=input('please input word')
f=open('dict.txt')
for line in f:
    if line.split(' ')[0]==word:
        print(line)
        break
    elif word<line.split(' ')[0]:
        print('no this word')
        break
f.close()
