"""
初识flask框架

"""

from flask import Flask,render_template,request
import pymysql

# 进行实例化
app = Flask(__name__)



@app.route("/")
def index11():
    sql = "select * from user"
    data = connect_mysql(sql)

    # 把数据放到html页面中
    return render_template("index.html",data=data)
            # 将数据返回到templates包中的某个页面，数据



# 定义视图，显示页面
@app.route("/add")
def addbook():
    # 显示留言添加的页面

    return render_template("add.html")



# 第一视图，接收表单数据，完成插入
@app.route("/insert",methods=['post'])
def insert():
    # 1.接收表单数据,在转化为字典形式
    data1 = request.form.to_dict()
    print(data1)

    # 2.插入数据库
    sql = f'insert into user values (null,"{data1["userName"]}","{data1["password"]}")'
    res = connect_mysql(sql)

    # 3.成功后跳转到图书显示页面
    if res:
        return '<script>alert("添加成功");location.href="/"</script>'
    else:
        return '<script>alert("添加成功");location.href="/add/"</script>'


    return "i love wang xiaojing"




@app.route("/delete")
def delete():
    # 获取点击的id
    id = request.args.get("id")
    # 1.准备sql语句
    sql = f"delete from user where id = {id}"

    # 2.执行sql语句
    res = connect_mysql(sql)

    # 3.检验结果
    if res:
        return '<script>alert("删除用户成功");location.href="/"</script>'
    else:
        return '<script>alert("删除用户失败");location.href="/"</script>'







def connect_mysql(sql):
    # 1.连接数据库
    db = pymysql.connect(host="localhost", user="root", password="1234", db="exam",
                         charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
    # 最后一个参数转为字典格式，默认为元组

    try:
        # 2.创建游标对象
        cursor = db.cursor()

        # 3.准备sql语句

        # 4.执行sql语句
        row = cursor.execute(sql)  # 得到改变mysql的行数
        db.commit()  # 提交事务

        # 5.提取结果
        data = cursor.fetchall()  # 将结果变为数组
        # data = cursor.fetchone()  #将结果变为字典
        if data:
            return data
        else:
            return row

    except:
        db.rollback()

    finally:
        # 6.关闭数据库
        db.close()




if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port="8080")










