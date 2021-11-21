# coding:utf-8

from django.urls import path
from TestModel import views

urlpatterns = [
    path('login/', views.login, name='login'),  # 添加名字方便修改地址
    path('s_index/', views.s_index, name='s_index'),
    path('history/', views.history, name='history'),
    path('s_logout/', views.s_logout, name='logout'),
]