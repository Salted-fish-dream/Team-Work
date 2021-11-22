from django.shortcuts import HttpResponse
from TestModel import models


def add_userinfo(user, address, link):
    demand = models.UserInfo.objects.create(userId=user, address=address, link=link)
    print(demand, type(demand))
    return HttpResponse("<p>数据添加成功！</p>")


def select_user(user, address):
    demand = models.UserInfo.objects.filter(userId=user, address=address)
    print(demand, type(demand))
    return HttpResponse("<p>数据查询成功！</p>")


def select_bird(bird_id):
    link = models.BirdsInfo.objects.filter(bird_id=bird_id).values("link")
    print(link[0]["link"])
    return HttpResponse("<p>鸟的链接查询ok！</p>")
