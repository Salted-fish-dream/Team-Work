import os
from pathlib import Path


def d_interface(pic, userId):
    # i 为运行模块次数 1,2,3,4，...
    # pic 为上传图片路径
    FILE = Path(__file__).resolve()  # 接口路径
    ROOT = FILE.parent
    weight_path = ROOT / 'runs/train/exp9/weights/best.pt'
    source_path = ROOT / 'data/VOC2007/JPEGImages/' / pic

    d_command = 'python detect.py --weight ' + str(weight_path) + ' ' + '--source ' + str(source_path)
    bat_path = Path('input.bat')  # 写入bat文件
    with bat_path.open('w+', encoding='utf-8') as f:
        f.writelines(d_command)
        f.writelines('\nexit')
    os.system('input.bat')

    result_path = str(ROOT) + 'runs/detect/' + userId + '/' + pic
    return result_path


d_interface('001.jpg', "xu")
