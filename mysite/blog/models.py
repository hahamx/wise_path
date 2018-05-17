#-*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

#admin.site.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    #使用列表显示结果
    list_display = ('title', 'timestamp')

class Meta():
    """
    字符串-timestamp是一个简洁的方式来告诉Django，“按时间戳”字段排序，并按降序执行。“（如果我们忽略了” - “，则会以升序日期顺序显示）。
    """
    ordering = ('-timestamp',)

admin.site.register(BlogPost, BlogPostAdmin)