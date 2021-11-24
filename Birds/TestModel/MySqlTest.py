from django.shortcuts import HttpResponse
from TestModel import models


def add_userinfo(user, address, link):
    demand = models.UserInfo.objects.create(userId=user, address=address, link=link)
    print(demand, type(demand))
    print("数据添加成功")


def select_history(user):
    demand = models.UserInfo.objects.filter(user=user).order_by('-time').all()[:5].values_list("address", "time")
    print(demand, type(demand))
    return demand


def select_bird(bird_id):
    link = models.BirdsInfo.objects.filter(bird_id=bird_id).values("link")
    return link[0]["link"]
