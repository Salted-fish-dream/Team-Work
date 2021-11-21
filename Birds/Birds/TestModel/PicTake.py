import base64
import os

import pymysql

# 获取数据库连接
database = pymysql.connect(user='root', password='', host='localhost', db='birdphoto')

# 获取游标对象
cursor = database.cursor()

# 定义sql语句
sql = "select * from Birds limit 1;"

# 执行sql语句
cursor.execute(sql)

# 获取返回值
rows = cursor.fetchall()

# 建立图片取出的文件夹
pic_take = os.getcwd() + "\\" + "pic_take"
if not os.path.exists(pic_take):
    os.makedirs(pic_take)

# 读取照片并使用base64解码
for row in rows:
    pic_sav_path = row[1]
    (pic_sav_path_, name) = os.path.split(pic_sav_path)
    name = name.split(".")[0]
    with open(pic_sav_path, 'rb') as fr:
        base64code = fr.read()
    with open(pic_take + "\\" + name + ".jpeg", "wb") as fw:
        fw.write(base64.b64decode(base64code))

cursor.close()
database.close()
