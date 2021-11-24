"""Birds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from TestModel import views

urlpatterns = [

    # 微信登录部分
    path('login/', views.Login),
    # 上传图片与返回链接部分
    path('s_index/', views.upload),
    # 查询历史记录部分
    path('history/', views.history),
    # path('api/login', views.Login.as_view(), name='login')

]
