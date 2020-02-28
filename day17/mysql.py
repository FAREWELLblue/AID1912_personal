'''
mysql.py
pymysql基本流程

'''
import pymysql
db=pymysql.connect(host = 'localhost',
                   port = 3306,
                   user = 'root',
                   password = '123456',
                   database = 'student',
                   charset = 'utf8')
# 创建游标（操作数据，执行sql语句，获取结果）
cur = db.cursor()

#执行各种操作
cur.execute('show tables;')

#关闭游标
cur.close()
db.close()
