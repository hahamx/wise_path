#coding:utf-8

#第二步是定义博客应用程序包本身中的URL。 制作一个包含以下行的新文件mysite / blog / urls.py：
#from django.conf.urls import url # is for django 1.3
#from django.conf.urls  import url       # is for django 1.4

from django.conf.urls import *
from views import archive


#正则匹配裸露的URL 如/blog/， archive为一级函数
#你应该看到一个简单的，裸体的渲染任何你已经输入的博客文章，完整的标题，时间戳和帖子的身体。
urlpatterns = ['.', url(r'^$', archive), ]