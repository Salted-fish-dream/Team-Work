import os
from pathlib import Path
import pathlib


def d_interface(pic, userId):
    # i 为运行模块次数 1,2,3,4，...
    # pic 为上传图片路径
    
    pwd = os.getcwd()  # 接口路径
    print(pwd)
    ROOT =os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    print(ROOT)
    weight_path = ROOT + '/runs/train/exp9/weights/best.pt'
    source_path = pic
    

    pic_temp = pic.split('.')[0]

    userId_temp = userId + pic_temp.split('/')[-1]


    

    d_command = 'python /root/anaconda3/envs/yolo/yolov5-master/detect.py --weight ' + str(weight_path) + ' ' + '--source ' + str(
        source_path) + ' ' + '--name ' + str(userId_temp)
    print("==============================\n")
    print("命令为："+d_command)

    bat_path = '/root/anaconda3/envs/yolo/yolov5-master/input.bat'  # 写入bat文件
   
    
    with open(bat_path, 'w+', encoding='utf-8') as f:
        f.writelines(d_command)
        f.writelines('\nexit')
    os.system(bat_path)

    result_path = ROOT + '/teamwork1/runs/detect/' + userId_temp + '/' + pic.split('/')[-1]
    print("result_path:  "+result_path)

    return result_path
