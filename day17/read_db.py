'''
read_db.py
数据库的查询操作
'''
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='student',
                     charset='utf8')
# 创建游标（操作数据，执行sql语句，获取结果）
cur = db.cursor()

# 查询数据库
sql='select name,age,score from cls where score>85;'
cur.execute(sql)

# 获取结果方法1
# for i in cur:
#     print(i)

# 获取结果方法2
# cur.fetchone()
# print(cur.fetchall())
print(cur.fetchmany(2))

# 关闭游标
cur.close()
db.close()
