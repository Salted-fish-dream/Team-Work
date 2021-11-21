from django.db import models


class UserInfo(models.Model):
    # 分别为用户的openid，原始图片的地址，图片对应信息的链接，以及查询的时间
    userId = models.CharField(max_length=100)
    address = models.FilePathField(max_length=100)
    link = models.JSONField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)


class BirdsInfo(models.Model):
    # 分别为鸟类的编号，名字，对应信息的链接
    birdId = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    link = models.JSONField(max_length=100)
