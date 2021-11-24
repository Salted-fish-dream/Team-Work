# Create your views here.


from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from requests import Response

from TestModel import wx_login
from TestModel.MySqlTest import select_bird, add_userinfo, select_history

from TestModel.input_interface import d_interface
from TestModel.output_interface import h_interface

import json

from TestModel.PicSave import save_file


# 微信登录
def Login(request):
    # 获得请求数据
    param = request.data
    if not param.get('code'):
        return JsonResponse({'status': 1, "msg": "缺少参数"})
    else:
        # 访问微信官网，得到用户的openid和session
        code = param.get('code')
        user_data = wx_login.get_login_info(code)
        if user_data:
            val = user_data['openid']
            return JsonResponse({
                'status': 0,
                'msg': 'ok',
                'data': {'token': val}
            })
        else:
            return JsonResponse({'status': 2, 'msg': "无效的code"})


# 开始处理图片，并返回结果
def upload(request):
    user = request.POST.get("openid")
    address = request.FILES.get("address")

    # 将图片输出到对应的路径下，将openid和address写入到session中
    request.session['openid'] = user
    request.session['address'] = save_file(user, address)
    # 开始执行算法
    # 调出txt结果路径，将算法执行后的结果数据地址返回
    result_path = h_interface(request.session.get('address'), request.session.get('openid'))

    #     这里是调用算法进行处理
    ####################################
    ####################################
    ####################################
    #####################################

    # 读取鸟类的种类
    with open(result_path, 'r', encoding='utf-8') as f:
        line = f.readline()

    # 查询数据库和插入数据库
    request.session['link'] = select_bird(line.split(" ")[0])
    add_userinfo(request.session.get('openid'), request.session.get('address'), request.session.get('link'))
    # 返回图片的链接和对应信息的连接
    return JsonResponse({'status': 0, 'pic_msg': request.session.get('address'), 'link_msg': request.
                        session.get('link')})


# 获取历史记录功能
def history(request):
    # 获取当前的用户的历史记录
    user = request.session.get('openid')

    obj = select_history(user)

    ret = json.dumps(list(obj), ensure_ascii=False)

    return HttpResponse(ret, content_type='application/json')
