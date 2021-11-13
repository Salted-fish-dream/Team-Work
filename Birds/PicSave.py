import pymysql
import base64
import os

# 获取用户信息...

# 为每个用户创建一个文件夹
sav_path = os.getcwd() + "\\" + "用户1"

if not os.path.exists(sav_path):
    os.makedirs(sav_path)

# 把base64生成到对应文件夹下面  然后把文件地址写入数据库
pic_path = 'photo/1.jpeg'  # ？？图片从哪里来？？
with open(pic_path, 'rb') as fp:
    img = base64.b64encode(fp.read())
fp.close()
pic_name = pic_path.split('/')[1].split('.')[0]
pic_sav_path = sav_path + "\\" + pic_name + ".txt"
print(pic_sav_path)
with open(pic_sav_path, "wb") as fw:
    fw.write(img)

# 存时存的是 用户和文件地址 用到图片时再用那个地址
database = pymysql.connect(user="root", password="245890", host="localhost", db="BirdPhoto", charset="utf8")
cursor = database.cursor()
sql = "insert into Birds values (%s,%s);"
args = ("user1", pic_sav_path)
cursor.execute(sql, args)
database.commit()
cursor.close()
database.close()
