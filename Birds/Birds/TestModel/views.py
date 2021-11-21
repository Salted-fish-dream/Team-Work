# Create your views here.
from turtle import forward

from django.shortcuts import redirect, render
from TestModel import models
from django.http import HttpResponse

import json

from TestModel.PicSave import save_file


def login(request):
    # 这里到时候会改
    if request.method == "GET":
        return render(request, "login.html")

    user = request.POST.get("user")
    address = request.FILES.get("address")

    # 输出获取的id和地址
    print(user)
    print(address)
    user_obj = models.UserInfo.objects.filter(user=user, address=address).first()

    request.session['user'] = user
    request.session['address'] = save_file(user, address)

    return redirect(s_index)


def s_index(request):
    user = request.session.get('user')

    # if not user:
    #     return redirect(login)
    if request.method == "GET":
        return render(request, "s_index.html")
    else:
        return redirect(history)


def s_logout(request):
    request.session.flush()  # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect('/session_login/')


def history(request):
    user = request.session.get('user')

    obj = models.UserInfo.objects.filter(user=user).values_list("address")
    print("========================================")
    ret = json.dumps(list(obj), ensure_ascii=False)
    print(ret)
    return HttpResponse(ret, content_type='application/json')
