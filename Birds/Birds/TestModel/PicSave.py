import os
import TestModel.MySqlTest
import datetime


# 获取用户信息...

# 为每个用户创建一个文件夹
def save_file(user, address):
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = address.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    sav_path = os.getcwd() + "\\" + user

    if not os.path.exists(sav_path):
        os.makedirs(sav_path)

    # 把base64生成到对应文件夹下面  然后把文件地址写入数据库

    pic_path = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + "." + file_suffix
    path_file = os.path.join(sav_path, pic_path)

    open(path_file, 'wb').write(address.file.read())

    # with open(address, 'wb') as fp:
    #     for chunk in address.chunks():
    #         fp.write(chunk)

    TestModel.MySqlTest.add_userinfo(user, '', path_file)

    return pic_path
