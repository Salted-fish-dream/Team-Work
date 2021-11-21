import os
from pathlib import Path


def d_interface(pic, userId):
    FILE = Path(__file__).resolve()  # 接口路径

    ROOT = FILE.parent
    weight_path = ROOT / 'runs/train/exp9/weights/best.pt'
    source_path = ROOT / 'data/VOC2007/test100/' / pic

    d_command = 'python detect.py --source ' + str(source_path) + ' ' + '--weight ' + str(weight_path) + ' --img 640 ' \
                                                                                                         '--save-txt'

    print(d_command)
    bat_path = Path('output.bat')  # 写入bat文件

    with bat_path.open('w+', encoding='utf-8') as f:
        f.writelines(d_command)
        f.writelines('\nexit')

    os.system('output.bat')

    txt_path = pic.split('.')[0] + '.txt'
    result_path = str(ROOT) + 'runs/detect/' + userId + '/labels/' + txt_path

    with open(result_path, 'r', encoding='utf-8') as f:
        line = f.readline()
    return line.split(" ")[0]


d_interface('002712.jpg', "xu")
