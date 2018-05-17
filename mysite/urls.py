#-*- coding:utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views


urlpatterns = [url(r'^blog/', include(admin.site.urls)),
                url(r'^$', views.archive), ]

"""
# 捕获博客中所有请求，并传递它们给您要创建的新的URL conf, 相当于flask的路由转跳
# blog路由到后台
#不输入任何页面时,主页默认显示内容
"""
