"""
操作mysql
   1.链接mysql数据库
   2.创建游标对象
   3.准备sql
   4.使用游标对象执行sql
   5.提取结果
   6.关闭数据库链接

"""

import pymysql

# 1.连接数据库
db = pymysql.connect(host="localhost",user="root",password="1234",db="exam",
                     charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
                                      # 最后一个参数转为字典格式，默认为元组

try:
    # 2.创建游标对象
    cursor = db.cursor()

    # 3.准备sql语句
    sql = "select * from user"
    # sql = "insert into user (id,userName,password) values (NULL,'zhang','123')"

    # 4.执行sql语句
    row = cursor.execute(sql)  # 得到改变mysql的行数
    db.commit()   # 提交事务

    # 5.提取结果
    data = cursor.fetchall()    #将结果变为数组
    # data = cursor.fetchone()  #将结果变为字典
except:
    db.rollback()

finally:
    # 6.关闭数据库
    db.close()

print(data)
print(row)
































