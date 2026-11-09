import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='jh010924')

cursor = connection.cursor()

# 创建资料库
cursor.execute("CREATE DATABASE `qq`;")

#取得所有资料库名称
#cursor.execute("SHOW DATABASES;")
#records = cursor.fetchall()
#for r in records:
#    print(r)

#选择资料库
#cursor.execute("USE `sql_tutorial`;")

#创建表格
#cursor.execute('CREATE TABLE `qq`(qq INT);')

cursor.close()
connection.close()