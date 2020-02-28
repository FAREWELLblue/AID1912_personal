'''
    建立一个dict表
    创建一个words表 id word mean
    将单词本中的单词加入到数据库
'''
import pymysql

db=pymysql.connect(host = 'localhost',
                   port = 3306,
                   user = 'root',
                   password = '123456',
                   database = 'dict',
                   charset = 'utf8')
# 创建游标（操作数据，执行sql语句，获取结果）
cur = db.cursor()

#执行各种操作
f = open('dict.txt','r')
try:
    for line in f:
        print(line.split(' ',1))
        sql="insert into words (word,mean) values (%s,%s);"
        print(sql)
        cur.execute(sql,[line.split(' ',1)[0], line.split(' ',1)[1].strip(' ')])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


#关闭游标
f.close()
cur.close()
db.close()