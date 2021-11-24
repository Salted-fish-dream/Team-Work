import os
from pathlib import Path
import pathlib


def h_interface(pic, userId):
    pwd = os.getcwd()  # 接口路径

    ROOT = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")

    weight_path = ROOT + '/runs/train/exp9/weights/best.pt'

    pic_temp = pic.split('.')[0]
    userId_temp = userId + pic_temp.split("/")[-1]

    
    source_path = pic
    print('source_path:'+source_path)
    print('weight_path:'+weight_path)


    d_command = 'python /root/anaconda3/envs/yolo/yolov5-master/detect.py --source ' + str(source_path) + ' --weights '+ str(weight_path) + ' --name ' +  userId_temp + ' --save-txt'
    
    print("=============================")
    print("命令为： "+d_command)
    
    
    bat_path = '/root/anaconda3/envs/yolo/yolov5-master/output.bat'  # 写入bat文件

    with open(bat_path,'w+', encoding='utf-8') as f:
        f.writelines(d_command)
        f.writelines('\nexit')

    os.system(bat_path)

    txt_path = pic_temp.split('/')[-1] + '.txt'

    result_path = ROOT + '/teamwork1/runs/detect/' + userId_temp + '/labels/' + txt_path
    
    print('result_path:'+result_path)

    return result_path
