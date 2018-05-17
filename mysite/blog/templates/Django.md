

mid.provess_view(request.view_func,view_args,view_kwargs,mid.provess_request(request))

============                      <---> model  <--->db

|URL Resolver|   --> view     <----> Django  template

============              |

​                          user<==|

mid.process_response(request.response)



MVC: Model View Controller

MTC:Model Template View,  Django

#启动一个开发模板



django-admin.py startproject mysite

cd mysite

manage.py runserver

Starting development server at http://127.0.0.1:8000/

admin.py

views.py

查看django版本：

python -c "import django; print(django.get_version())"

-------------------------------------------------------------------------------------------

### 示例：使用Django 三个小时发布一个blog

```python
​```
本章的所有工作都是在您选择的shell（bash，tcsh，zsh，Cygwin或您有什么）的命令行上完成的。 所以打开你的终端和cd到你的PYTHONPATH环境变量的目录。 在基于Unix的系统（如Linux，Mac OS X，FreeBSD等）上，您可以发出echo $ PYTHONPATH命令(我是用whereis python查看的)查看其内容; 从Win32命令窗口中，键入echo％PYTHONPATH％。 您可以在安装和Python章节中阅读有关路径的更多信息。
如果在执行过程中，出现无法解决的错误建议退回三步，或删除项目重来，这样更节省时间
​```
```



1,安装虚拟机

2,修改语言设置 locale,   locale   -a,   LANG=

3安装pip   https://pypi.python.org/pypi/pip/9.0.1

- linux中，whereis python 查找到python目录
- 拷贝到环境：/usr/lib/python2.7/site-packages
- python2.7 可直接安装（低版本python需要先安装setuptools）
- 解压pip包， tar -zxvf pip.tar.gz

```pthon
cd pip-9.0.1/
python setup.py install
 pip --version
pip 9.0.1 from /usr/lib/python2.7/site-packages/pip-9.0.1-py2.7.egg (python 2.7)

```

```python
'''
当您开始使用Django代码时，最简单的组织Django代码的方法就是使用Django调用一个项目：通常是一个单一网站构成的文件目录。 Django附带一个名为django-admin.py的实用程序来简化诸如创建这些项目目录之类的任务。 在Unix上，它将默认安装到/ usr / bin目录中，如果您使用的是Win32，则可以直接进入Python安装中的Scripts文件夹，例如C：\ Python25 \ Scripts。 在这两种情况下，您需要确保django-admin.py位于PATH中，以便可以从命令行执行。
要为您的博客项目创建项目目录，请发出此django-admin.py命令：
django-admin.py startproject mysite
'''
```

```shell
[root@localhost /usr/bin]# ll | grep django
-rwxr-xr-x.   1 root root        266 4月   4 11:26 django-admin
-rwxr-xr-x.   1 root root        124 4月   4 11:26 django-admin.py
-rw-r--r--.   1 root root        305 4月   4 11:26 django-admin.pyc

[root@localhost bin]# django-admin.py startproject mysite
```

```python
'''
在Win32框上，您需要首先打开DOS命令窗口。 可以通过开始 - >程序 - >附件 - >命令提示符访问。 另外，代替$，您会看到像C：\ WINDOWS \ system32>一样的shell提示符。

现在看看目录的内容，看看这个命令为你创建了什么。 在Unix上应该看起来像这样：
$ cd mysite
$ ls -l
total 24
-rw-r--r--    1 pbx  pbx     0 Jun 26 18:51 __init__.py
-rwxr-xr-x    1 pbx  pbx   546 Jun 26 18:51 manage.py
-rw-r--r--    1 pbx  pbx  2925 Jun 26 18:51 settings.py
-rw-r--r--    1 pbx  pbx   227 Jun 26 18:51 urls.py
'''
```

```python
[root@localhost mysite]# pwd
/home/linux/mysite/mysite
[root@localhost mysite]# ll
总用量 28
-rw-r--r--. 1 root root    0 4月   4 12:26 __init__.py
-rw-r--r--. 1 root root  124 4月   4 12:31 __init__.pyc
-rw-r--r--. 1 root root 3096 4月   4 12:26 settings.py
-rw-r--r--. 1 root root 2552 4月   4 12:31 settings.pyc
-rw-r--r--. 1 root root  763 4月   4 12:26 urls.py
-rw-r--r--. 1 root root  967 4月   4 12:31 urls.pyc
-rw-r--r--. 1 root root  390 4月   4 12:26 wsgi.py
-rw-r--r--. 1 root root  580 4月   4 12:31 wsgi.pyc
#进入mysite目录， manage.py 为管理文件，使用python manage.py可查看所有命令
python manage.py runserver 18282
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

April 04, 2017 - 04:31:48
Django version 1.10.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:18282/
Quit the server with CONTROL-C.

```



#### 3，项目目录

```python
1.wsgi.py

wsgi（Python Web Server Gateway Interface）即Python服务器网关接口，是python应用与Web服务器之间的接口。

2.urls.py

URL配置文件。Django项目中所有地址（页面）都需要我们去配置URL。

3.settins.py

BASE_DIR:项目的根目录；
SECRET_KEY:安全码；
DEBUG:调试，实际生产中需要将其值设置为 false ；
ALLOWED_HOSTS:设置允许的外界访问的地址；
INSTALLED_APPS:记录加载的应用；
MIDLEWEAR:自带的工具集；
ROOT_URLCONF:URL根文件的配置文件；
TEMPLATES:模板文件，模板指的是一个个HTML文件；
WSGI_APPLICATION:
DATABASES:数据库文件，默认是sqlite3，如果要使用其他数据库可以到Django官网有关数据库配置的文档了解；
AUTH_PASSWORD_VALIDATORS：与密码认证有关；
LANGUAGE_CODE:语言，默认是un-es即美式英语；
TIME_ZONE:时区；
STATIC_URL:静态文件（CSS，JavaScript，images等）的地址。
4.init.py

声明模块，内容默认为空。
#创建应用
打开命令行，进入项目manage.py的同级目录     
输入：
python manage.py startapp blog
添加应用名到settings.py中的INSTALLED_APPS中（应用名不可以与模块名相同） 
'mysite.blog',
```

应用目录介绍

```python
'''
# cd blog
[root@localhost blog]# ll
总用量 32
-rw-r--r--. 1 root root  63 4月   4 12:36 admin.py     #该应用的后台管理系统
-rw-r--r--. 1 root root 179 4月   4 12:42 admin.pyc
-rw-r--r--. 1 root root 124 4月   4 12:36 apps.py      #该应用的一些配置，Django-1.9以后自动生成
-rw-r--r--. 1 root root   0 4月   4 12:36 __init__.py
-rw-r--r--. 1 root root 122 4月   4 12:42 __init__.pyc
drwxr-xr-x. 2 root root  45 4月   4 12:42 migrations      # 一个数据迁移的模块，内容自动生成
-rw-r--r--. 1 root root  98 4月   4 12:36 models.py      #数据模块，使用ORM框架
-rw-r--r--. 1 root root 240 4月   4 12:42 models.pyc
-rw-r--r--. 1 root root  60 4月   4 12:36 tests.py      #自动化测试的模块
-rw-r--r--. 1 root root  63 4月   4 12:36 views.py     #执行响应的代码所在模块，是代码逻辑处理的主要地点，项目中大部分代码在这里编写
'''
应用程序也是一个包。 models.py和views.py文件中没有真正的代码; 他们只是占位符。 对于我们的简单博客，其实我们根本不需要触摸虚拟的views.py文件。

要告诉Django这个新应用程序是您的项目的一部分，您需要编辑settings.py（我们也可以将其称为“设置文件”）。 在编辑器中打开设置文件，并在底部找到INSTALLED_APPS元组。 将您的应用程序以点状的模块形式添加到该元组中，该行类似于此（注意尾部的逗号）：
'mysite.blog'，  # mysite\blog folder on windows
```

#### 启动项目:

```python
1,修改setting配置:ALLOWED_HOSTS  = "*"
2,python manage.py runserver 0.0.0.0:18282

```

```python
'''
startproject命令创建的每个文件都是Python源代码。 没有XML，没有.ini文件，没有时髦的配置语法。 Django尽可能追求“纯Python”哲学。 这给了您很大的灵活性，而不会增加框架的复杂性。 例如，如果您希望您的设置文件从某个其他文件导入设置或计算一个值而不是将其编码为硬编码，那就没有障碍 - 它只是Python。
'''
```

#### 编辑项目

```python
blog中models
#-*-coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
'''
这是一个完整的模型，代表一个具有三个字段的“BlogPost”对象。 （实际上，严格来说，它有四个字段 - Django默认为每个模型自动创建一个自动递增的唯一ID字段。）

你可以看到我们新建的类，BlogPost，是django.db.models.Model的子类。 这就是Django数据模型的标准基类，它是Django强大的对象关系映射系统的核心。 此外，您注意到我们的字段被定义为常规类属性，每个属性都是特定字段类的一个实例。 这些字段类也在django.db.models中定义，并且，比我们在这里使用的三种类型还有更多的类型，从BooleanField到XMLField。

许多人使用Django与关系数据库服务器，如PostgreSQL或MySQL。 这里有六个可能相关的设置（尽管您可能只需要两个）：DATABASE_ENGINE，DATABASE_NAME，DATABASE_HOST，DATABASE_PORT，DATABASE_USER和DATABASE_PASSWORD。 他们的名字使他们各自的目的相当明显。 只需插入与Django使用的数据库服务器对应的正确值。 例如，MySQL的设置如下所示：

DATABASE_ENGINE =“mysql”
DATABASE_NAME =“djangodb”
DATABASE_HOST =“localhost”
DATABASE_USER =“paul”
DATABASE_PASSWORD =“小马”  ＃密码！

我们没有指定DATABASE_PORT，因为只有在数据库服务器运行在非标准端口上时才需要这样做。 例如，MySQL的服务器默认使用端口3306。 除非您更改了设置，否则您根本不必指定DATABASE_PORT。

SQLite是一个受欢迎的选择，用于测试甚至部署在没有大量同步写入的场景中。 不需要主机，端口，用户或密码信息，因为SQLite使用本地文件系统进行存储以及访问控制的本机文件系统权限。 所以只需要两个设置来告诉Django使用你的SQLite数据库。

DATABASE_ENGINE = "sqlite3"
DATABASE_NAME = "/var/db/django.db"

当使用SQLite与真正的Web服务器（如Apache）时，您需要确保拥有Web服务器进程的帐户对数据库文件本身和包含该数据库文件的目录具有写入权限。 当我们在这里使用dev服务器时，权限通常不是一个问题，因为运行dev服务器的用户（您）也拥有项目文件和目录。
SQLite也是Win32平台最受欢迎的选择之一，因为它可以免费使用Python发行版。 鉴于我们已经使用我们的项目（和应用程序）创建了一个C：\ py \ django目录，我们来创建一个db目录。
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = r'C:\py\django\db\django.db'
'''
./manage.py migrate           # or ".\manage.py migrate" on win32  django 1.9以上需要用此命令
```

```json
'''
当您发出migrate命令时，Django会在每个INSTALLED_APPS中查找一个models.py文件。 对于每个找到的模型，它创建一个数据库表。 （稍后，当我们进入诸如多对多关系的花哨的东西时，有例外，但是这个例子是正确的，如果你使用SQLite，你也会注意到django.db数据库文件是在你指定的地方创建的 。）

INSTALLED_APPS中的其他项目，默认的那些项目都有模型。 来自manage.py syncdb的输出证实了这一点，您可以看到Django为每个应用程序创建一个或多个表。

但是，并不是所有从migrate命令得到的输出。 您还有一些与django.contrib.auth应用程序相关的交互式查询。
'''
```

创建表操作记录

```python

C:\Python27\Scripts\mysite>manage.py migrate
C:\Python27\Scripts\mysite
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK

'''
您的初始数据库设置现已完成。 下次在此项目上运行migrate命令（您随时添加应用程序或模型时），您会看到输出少一些，因为它不需要再次设置任何这些表或提示您 创建一个超级用户。
'''
```

#### 设置自动管理应用程序

自动后端应用程序或管理员已经被描述为Django的“皇冠宝石”。对于那些厌倦了为Web应用程序创建简单的“CRUD”（创建，读取，更新和删除）界面的人来说，这是一个天赋。 我们在第11章“高级Django编程”中的“自定义管理”中进一步了解管理员。现在，让我们把它打开一下。

由于它是Django的可选部分，因此您需要在您正在使用的settings.py文件中指定 - 就像您使用自己的博客应用一样。 打开settings.py并将以下行添加到INSTALLED_APPS元组，就在'django.contrib.auth'下面。

```pyhton
django默认已有
'django.contrib.admin',

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite.blog',
]
```

每次将新应用程序添加到项目中时，都应运行migrate命令，以确保在数据库中创建了所需的表。 在这里，我们可以看到将管理应用程序添加到INSTALLED_APPS并运行migrate触发器在我们的数据库中再创建一个表

现在应用程序已经设置好了，我们需要做的就是给它一个URL，以便我们可以得到它。 你应该注意到这两行在你自动生成的urls.py中。



从第二行删除＃字符（并且您可以同时删除第一个仅注释行）并保存该文件。您已经告诉Django加载默认的管理员站点，这是一个由contrib管理员应用程序使用的特殊对象。

```python
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

最后，您的应用程序需要告诉Django哪些模型应该显示在管理屏幕中进行编辑。为此，您只需要定义之前提到的默认管理站点，并使用它注册您的BlogPost模型。打开mysite / blog / models.py文件，确保导入管理应用程序，然后在底部添加注册模型的行。

```python
from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

admin.site.register(BlogPost)
```



管理员的简单使用是冰山一角;可以通过为给定模型创建一个特殊的Admin类来指定许多不同的管理相关选项，然后使用该类注册模型。我们很快就会做到这一点，你也可以在后面的章节中看到高级管理员使用的例子，特别是在第三部分“Django应用程序示例”中，第四部分是“高级Django技术和特性”。

```python
#创建管理员
$ python manage.py createsuperuser
#输入你想使用的用户名，然后回车。
Username: root
#邮箱
Email address: admin@example.com
#最后一步是输入密码。你会被要求输入两次密码，第二次的目的是为了确认第一次输入的确实是你想要的密码。
Password: ********       #root@123
Password(again): ********     #root@123
Superuser created successfully.
```



现在使用http://192.168.0.102:18282/admin 登陆管理后台

尝试管理员
现在，我们已经使用管理员应用程序设置了Django站点，并注册了我们的模型，我们可以将其重新启动一下。 再次发出manage.py runserver命令。 现在，在Web浏览器中，访问http://127.0.0.1:8000/admin/。 （不要担心，如果您的开发者服务器地址不同，只需添加一个管理员，就可以了。）您应该看到一个登录屏幕，如图2.4所示。

# [Django administration](http://192.168.0.102:18282/admin/)

Username: Password:  

#### 可能的问题

“我的应用程序不显示在管理员”的三个最常见的原因是，问题是

- 1）忘记使用admin.site.register注册模型类，
- 2）应用程序的models.py中的错误，
- 3）忘记 将该应用程序添加到settings.py文件中的INSTALLED_APPS元组中。

使用超级用户登陆后

```python
可执行发帖操作
```

只需要记住，改变模型需要这三步，新建blog时，需要执行以下三步

- 编辑 **models.py** 文件，改变模型。
- 运行 `python manage.py makemigrations` 为模型的改变生成迁移文件。
- 运行 `python manage.py migrate` 来应用数据库迁移



```python
开发服务器注意到您的更改并重新加载您的模型文件。 如果你正在监视你的命令shell，你会看到一些这样的输出。

如果您刷新页面，现在您可以根据添加到您的BlogPostAdmin类的新的list_display变量看到更多有用的输出 

尝试点击已出现的标题和时间戳列标题 - 每个都会影响您的项目的排序方式。 例如，在标题上点击一次，按标题升序排列; 再次单击标题标题更改为降序。

管理员有许多其他有用的功能，只需一行或两行代码即可激活：搜索，自定义排序，过滤器等。 如我们已经提到过的，第三部分和第四部分更详细地介绍或展示了许多这些话题。
```

### 对外发布博客

```python
'''
让你的博客公共访问
随着我们应用程序的有了数据库和管理员端的功能，现在是时候转向面向公开的页面。 Django的一个页面有三个典型的组件：
显示传递给它的信息的模板（在类似于Python的类字典中，称为上下文）
通常从数据库中获取要显示的信息的视图功能
将传入请求与视图功能相匹配的URL模式，也可以将参数传递给视图
我们将按顺序处理这三个。 从某种意义上说，这是从内部构建的，当Django处理请求时，它以URL模式开始，然后调用视图，然后将渲染的数据返回到模板中。

创建模板
Django的模板语言很容易读取，我们可以直接跳到示例代码。 这是一个显示单个博文的简单模板：
template中创建html，   mysite/blog/templates/archive.html

'''
```

```python
 mysite/blog/templates/archive.html
    #在变量标签中，您可以使用Python风格的点表示法来访问传递给模板的对象的属性
{% for post in posts %}             ##Django的模板标签
<h2>{{ post.title }}</h2>           #该模板假设您已经传递了一个名为“post”的BlogPost对象。
<p>{{ post.timestamp }}</p>         #模板的三行分别提取了BlogPost对象的标题，时间戳和正文字段。
<p>{{ post.body }}</p>
{% endfor %}

```



第一步就像启用管理员一样。 在mysite / urls.py中，有一个注释的示例行，几乎是我们需要的。 编辑它看起来像这样：

#### 在blog中views.py创建博客视图函数

编写一个简单的视图函数，从数据库中获取我们所有的博客文章，并使用我们的模板显示它们。

 打开blog / views.py文件并键入以下内容：

```python
from django.template import loader, Context
from django.http import HttpResponse
from mysite.blog.models import BlogPost

def archive(request):

    """
    第0行：每个Django视图函数都将django.http.HttpRequest对象作为其第一个参数。它还可以通过URLconf传递其他参数，这是您正在使用的功能。
    第1行：当我们创建BlogPost类作为django.db.models.Model的子类时，我们继承了Django对象关系映射器的全部功能。该行是使用ORM（对象关系映射器;请参见第3章“启动”和“更多”）的一个简单示例，以获取数据库中的所有BlogPost对象。
    第2行：要创建我们的模板对象t，我们只需要告诉Django模板的名字。因为我们已经存储在我们应用程序的templates目录中，Django可以在没有进一步的指导的情况下找到它。
    第3行：Django模板渲染在上下文中提供给他们的数据，一个类似字典的对象。我们的上下文c只有一个键和值。
    第4行：每个Django视图函数返回一个django.http.HttpResponse对象。在最简单的情况下，我们传递构造函数一个字符串。模板渲染方法方便地返回一个字符串。
    """
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))
```

我们可以直接在mysite / urls.py内创建所需的URL模式，但这会在我们的项目和我们的应用程序之间产生混乱的耦合。 我们可以在其他地方使用我们的博客应用程序，让它负责自己的URL

```python
#第二步是定义博客应用程序包本身中的URL。 制作一个包含以下行的新文件mysite / blog / urls.py：
from django.conf.urls.defaults import ... # is for django 1.3
from django.conf.urls  import ...         # is for django 1.4

from django.conf.urls import *
from mysite.blog.views import archive
urlpatterns = （''，
     url（r'^ $'，archive），
）
```



模板的继承，可以让模板更简单

如果我们的网站有博客，照片存档和链接页面，我们希望所有这些都是基于一个共同的基础？经验告诉你错误的方法是将其复制并粘贴到三种相同的自包含模板中，Django中正确的方法是创建基本模板，然后扩展此模板以生成其他特定模板。在您的mysite / blog / templates目录中，创建一个名为base.html的模板，其中包含以下内容：

```python
base.html
<html>
<style type="text/css">
body { color: #efd; background: #453; padding: 0 5em; margin: 0 }
h1 { padding: 2em 1em; background: #675 }
h2 { color: #bf8; border-top: 1px dotted #fff; margin-top: 2em }
p { margin: 1em 0 }
</style>
<body>
<h1>mysite.example.com</h1>
{% block content %}
{% endblock %}
</body>
</html>
```

不完全是有效的XHTML格式，但它可以正常工作。 要注意的细节是{％block ...％}标签。 这定义了子模板可以改变的命名区域。 要使您的博客应用程序使用此模板，请更改您的archive.html模板，以便引用此新的基本模板及其“内容”块。

```python
archive.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% extends "base.html" %}
{% block content %}
{% for post in posts %}
<h2>{{ post.title }}</h2>
<p>{{ post.timestamp }}</p>
<p>{{ post.body }}</p>
{% endfor %}
{% endblock %}
</body>
</html>
```

{％extends ...％}标签告诉Django查找名为base.html的模板，并将此模板中的任何命名块的内容插入到该模板中的相应块中。 你现在应该看到类似图2.10的东西（希望你的博客文章更令人兴奋）。



我们可以向我们的模型添加默认排序，或者我们可以将其添加到我们的视图代码中的BlogPost.objects.all（）查询中。 在这种情况下，该模型是一个更好的位置，因为我们最经常要求的帖子按时间顺序排列。 如果我们在模型中设置我们首选的顺序，则访问我们的数据的Django的任何部分都使用该排序。

要为模型设置默认排序，请给它一个名为Meta的内部类，并在该类中设置排序属性。

```python
class Meta():
    ordering = ('-timestamp',)
```

如果您在逗号后添加“标题”，并且您有两个标题为“A”和“B”的帖子具有相同的时间戳，则“A”将发布。

要将过滤器应用于变量，您只需使用垂直条或“管道”字符将其放在变量名称的末尾（大括号内）

```
<p>{{ post.timestamp|date:"l, F jS" }}</p>        
#如果要显示星期几但省略年份，请更改行以将参数传递到日期过滤器
```

 第3章详细介绍了Django的关键组成部分和背后的哲学，并提供了一些Web开发原则，它们不仅适用于Django本身，还涉及本书后面部分的课程。 第4章，您将了解框架的细节，在那里您可以找到有关“如何，为什么以及如何...”的问题的答案，这可能是在您浏览上述示例时出现的。 在第4章之后，您有足够的理解来跟踪并构建几个示例应用程序：内容管理系统，pastebin，照片库和Ajax提供的“实时博客”。

# Django for the Impatient: Building a Blog