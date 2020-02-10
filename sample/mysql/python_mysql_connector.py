# coding:utf-8
# [转载-Python与数据库](https://www.jianshu.com/p/002ab5acdaf1)
import mysql.connector

# 1.连接到数据库
mydb = mysql.connector.connect(
    host="10.50.181.9",
    port="3306",
    user="anti",
    passwd="anti",
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
# 2.删除数据表
sql = "DROP TABLE IF EXISTS anti.test"
mycursor.execute(sql)

# 3.创建数据表 其中id是整型，而name是字符串.
mycursor.execute("CREATE TABLE anti.test (id INT, name VARCHAR(255))")
# 4.插入信息
sql = "INSERT INTO anti.test (id, name) VALUES (%s, %s)"
val = ("1", "wenzi")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "success")

data_id = "1"
sql = "SELECT * FROM  anti.test WHERE id = '" + data_id + "'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 6.删除信息
sql = "DELETE FROM anti.test WHERE id = '001'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "delete")
