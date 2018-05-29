### 0,py解释器

```python

   程序执行-编码
          -解释器解释运行-字节码编译
                        -PVM(Python Virtual Machine)
```





### 1. 包升级更换

```python
#列出可升级的包
pip list --outdate
#升级一个包
pip install --upgrade locustio
#升级所有包
$ for i in `pip list -o --format legacy|awk '{print $1}'` ; do pip install --upgrade $i; done

$ pip freeze --local | grep -v '^-e' | cut -d = -f 1  | xargs -n1 pip install -U
#更换升级源
vim ~/.pip/pip.conf
[global]
trusted-host = mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple
#指定单次安装源
pip install <包名> -i http://pypi.v2ex.com/simple

#指定全局安装源

#在unix和macos，配置文件为：$HOME/.pip/pip.conf
#在windows上，配置文件为：%HOME%\pip\pip.ini
 
#linux升级所有包
$pip install -U distribute && pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U --allow-external mysql-connector-python
#查询可升级的包

pip list -o

#下载包而不安装

pip install <包名> -d <目录> 或 pip install -d <目录> -r requirements.txt

#打包
pip wheel <包名>

Successfully installed cycler-0.10.0 functools32-3.2.3.post2 matplotlib-2.0.1 numpy-1.12.1 python-dateutil-2.6.0 pytz-2017.2



```



#### 1.1 python升级

```python
#linux python2.7重新配置，安装Tkinter

#目的：既保证原有安装包的使用，又能重新编译使Tkinter可用
/home/tops/lib/python2.7/
	备份原有的python2.7 sudo mv
	1，下载安装包  https://www.python.org/downloads/release/python-278/
		Python-2.7.8.tgz
	2，拷贝并解压
		tar -zxvf Python-2.7.8.tgz
		sudo mv Python-2.7.8 python2.7
		cd python2.7
		2.1 vim Modules/Setup.dist
			找到下面这几行，把前面的井号去掉打开它
			_tkinter _tkinter.c tkappinit.c -DWITH_APPINIT \
			-L/usr/local/lib \
			-I/usr/local/include \
			-ltk8.5 -ltcl8.5 \
			-lX11
		2.2 第四行-ltk8.5 -ltcl8.5 默认是 8.2 ，请你系统实际tcl/tk版本修改

			[admin@AT111_AG:/home/tops/lib/python2.7] [cn-hangzhou-at111:cn-hangzhou-test-108:io8:classic:3880:river]
				$ rpm -qa | grep ^tk
				tk-8.4.13-5.1.alios5.1
				tk-8.4.13-5.1.alios5.1
				tk-devel-8.4.13-5.1.alios5.1
				tk-devel-8.4.13-5.1.alios5.1
				$ rpm -qa | grep ^tcl
				tcl-8.4.13-4.2.alios5
				tcl-devel-8.4.13-4.2.alios5
				tcl-devel-8.4.13-4.2.alios5
				tcl-8.4.13-4.2.alios5
			检测是否安装tcl-devel tk-devel

			rpm -qa | grep ^tcl-devel
			tcl-devel-8.4.13-4.2.alios5
			tcl-devel-8.4.13-4.2.alios5
			$ rpm -qa | grep ^tk-devel
			tk-devel-8.4.13-5.1.alios5.1
			tk-devel-8.4.13-5.1.alios5.1
		2.3 开始配置安装
		[admin@AT111_AG:/home/tops/lib/python2.7] [cn-hangzhou-at111:cn-hangzhou-test-108:io8:classic:3880:river]
				$ ldconfig
				$ ./configure
				...
				$ make
				...
				$ make install
		2.4 测试是否可正常使用
		新版
		[admin@AT111_AG:/home/tops/lib/python2.7] [cn-hangzhou-at111:cn-hangzhou-test-108:io8:classic:3880:river]
		$ python2.7
		Python 2.7.8 (default, May 10 2017, 10:58:03)
		[GCC 4.1.2 20080704 (Red Hat 4.1.2-46)] on linux2
		Type "help", "copyright", "credits" or "license" for more information.
		>>> import Tkinter
		>>>
		[21]+  Stopped                 python2.7
		旧版
		[admin@AT111_AG:/home/tops/lib/python2.7] [cn-hangzhou-at111:cn-hangzhou-test-108:io8:classic:3880:river]
		$ python
		Python 2.5.4 (r254:67916, May 31 2010, 15:03:39)
		[GCC 4.1.2 20080704 (Red Hat 4.1.2-46)] on linux2
		Type "help", "copyright", "credits" or "license" for more information.
		>>> import Tkinter
		>>>
		[22]+  Stopped                 python

		2.5 拷贝备份的库文件到新安装python环境
		sudo cp -R ../python2.7bak/* ./
       
#四、升级Python引起yum版本无法使用的问题解决

#不少童鞋安装后就

cp python /usr/bin/python

#导致yum时就提示

[root@lee ~]# yum
There was a problem importing one of the Python modules
required to run yum. The error leading to this problem was:

   No module named yum

Please install a package which provides this module, or
verify that the module is installed correctly.

It's possible that the above module doesn't match the
current version of Python, which is:
2.7.4 (default, Apr  9 2013, 17:12:56) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)]

If you cannot solve this problem yourself, please go to 
the yum faq at:
  http://yum.baseurl.org/wiki/Faq
  

[root@lee ~]# 

#因为yum头部默认制定python脚本的路径就是

#! /usr/bin/python

#你把旧版的python替换后就是用不了，不知道为何新版Python不能被yum识别，目前唯一最好解决的方法就是修改yum头部声明

vim /usr/bin/yum 改成

#! /usr/bin/python2.6

#即可，这里的python2.6是我centos默认版本，大家的默认版本是多少请按实际情况修改即可
		
```



### 2. 获取本机地址

```python
import socket
socket.gethostbyname(socket.gethostname())
```

### 2.1. 获取上级目录

```python
Path = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), os.path.pardir))
```

### 3. 解决自身python包不能被找到的问题&与环境设置

```python

#确保环境变量正常
#库路径
/home/tops/lib/python2.7/site-packages/
#bash设置
export PYTHONPATH=$PYTHONPATH:/home/tops/lib/python2.7/site-packages/
#查看系统路径需包含 /home/tops/lib/python2.7
echo $PATH
#查看PYTHON路径
echo $PYTHONPATH
:/home/tops/lib/python2.7/site-packages/
#查看当前python2.7路径
$ which python2.7
/usr/local/bin/python2.7

#永久添加变量，所有用户生效修改/etc/profile, 只对当前用户生效~/.bashrc
#添加代码：

export PATH=$PATH:/home/tops/lib/python2.7/site-packages/
export PYTHONPATH=$PYTHONPATH:/home/tops/lib/python2.7/site-packages/

#跟随项目自动添加python工作目录到sys.path
	1 import sys
	2 查看sys.path
	3 添加sys.path.append("/home/admin/testxyd/ocean-test")
#临时办法：添加python工作目录到PYTHONPAHT
export PYTHONPATH=$PYTHONPATH:/home/admin/testxyd/ocean-test
#永久固定目录办法：添加包目录到python2.7环境/home/admin/testxyd/ocean-test
sudo vim /home/tops/lib/python2.7/site-packages/mypkpath.pth

#查看
$ echo $PYTHONPATH
:/home/tops/lib/python2.7/site-packages/:/home/admin/testxyd/ocean-test

[admin@AT111_AG:/home/admin/testxyd/ocean-test] [cn-hangzhou-at111:cn-hangzhou-test-108:io8:classic:3880:river]
$ echo $PATH
/usr/ali/bin:/usr/ali/sbin:/usr/local/bin:/usr/local/sbin:/home/admin/bin:/home/admin/sbin:/opt/taobao/java/bin:/sbin:/usr/ali/bin:/usr/ali/sbin:/usr/local/bin:/usr/local/sbin:/home/admin/bin:/home/admin/sbin:/opt/taobao/java/bin:/sbin:/home/admin/taiwei/go/bin:/usr/kerberos/bin:/usr/ali/bin/:/usr/ali/sbin/:/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/bin:/usr/bin:/usr/X11R6/bin:/home/tops/bin:/opt/tdc:/apsara/river/:/apsara/deploy/:/apsara/river/:/apsara/deploy/:/home/tops/lib/python2.7:/home/tops/lib/python2.7/site-packages/
```



### 4. 数组与列表映射，多变量赋值

```python
#list映射，多变量赋值

["%s=%s" % (k, v) for k, v in params.items()]

#快速修改列表的所有值
li =[1,4,2,3]
>>> li2 = [x*2 for x in li]
>>> li2
[2, 8, 4, 6]
```



### 5. 调用命令行与环境

```python
python [-BdEiOQsRStuUvVWxX3?] [-c command | -m module-name | script | - ] [args]
Command line and environment
#called with -m module-name 参数m执行前先解析整个输入
python2.7 -m failover.testFO_suite
#called with -c command ，参数c执行给出的python作为命令，可能包括换行符分割多个语句
python  -c print(9+2),(1-3)
#当使用文件名参数或文件作为标准输入调用时，它将从该文件读取并执行脚本。
python -c   "import sys;print sys.path"
#当使用目录名参数调用时，它从该目录读取并执行适当命名的脚本。
```



### 6，CGIHTTPServer

```shell
#启用
$ nohup python2.7 -m CGIHTTPServer 18010 &
[1] 169024
nohup: appending output to `nohup.out'
#查看
ps -ef | grep python

admin    169024 160773  0 10:21 pts/2    00:00:00 python2.7 -m CGIHTTPServer 18010

```

​	



#### 7,字符串链接分割

```python
#链接，只能是字符串的list，有其他类型将报错
>>> params = {'name':'li','age':12,'sex':'man'}
>>> print ";".join(["%s=%s" % (k, v) for k, v in params.items()])
age=12;name=li;sex=man
#分割
>>> str1 = 'age=12;name=li;sex=man'
>>> print str1.split(';')
['age=12', 'name=li', 'sex=man']

```





#### 8, py常见10个坑

```python
#1,可选参数默认值的设置在Python中只会被执行一次，也就是定义该函数的时候
  def foo(bar=[]):        # bar是可选参数，如果没有提供bar的值，则默认为[]，
  ...    bar.append("baz")    # 但是稍后我们会看到这行代码会出现问题。
  ...    return bar
  >>> foo()
  ["baz"]
  >>> foo()
  ["baz", "baz"]
#解决办法
  def foo(bar=None):
  ...    if bar is None:    # or if not bar:
  ...        bar = []
  ...    bar.append("baz")
  ...    return bar
  >>> foo()
  ["baz"]
  >>> foo()
  ["baz"]

#2 错误使用继承类的变量
class A(object):
...     x = 1
>>> class B(A):
...     pass
>>> class C(A):
...     pass
B.x = 2
>>> print A.x, B.x, C.x
1 2 1

>>>A.x = 3
>>> print A.x, B.x, C.x
3 2 3
"""
类变量是以字典的形式进行处理的，并且遵循方法解析顺序（Method Resolution Order，MRO）。因此，在上面的代码中，由于类C中并没有x这个属性，解释器将会查找它的基类（base class，尽管Python支持多重继承，但是在这个例子中，C的基类只有A）。换句话说，C并不没有独立于A、真正属于自己的x属性。所以，引用C.x实际上就是引用了A.x。如果没有处理好这里的关系
"""

#3 在遍历列表时更改列表
odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> for i in range(len(numbers)):
...     if odd(numbers[i]):
...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
...
Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
IndexError: list index out of range
#解决办法
>>> bool(3%2)
True
>>> od = lambda x : bool(x%2)
>>> numbers = [i for i in range(10)]
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers[:] = [i for i in numbers if not od(i)]
>>> numbers
[0, 2, 4, 6, 8]
```

### 9, IDLE

- TAB 填充
- win Alt + P  与 Alt +N，Mac Ctrl+P， Ctrl+N
- 调整首选项符合你自己



### 10 ,pickle 持久存储与 with  as

用dump保存，用load恢复 #

```python
#pickle 只适用与python，通用格式有很多如json, yaml...
#数据储存时变更结构
import pickle
>>> with open('mydata.pickle','wb') as mysavedata:
	pickle.dump([1,2,'three'], mysavedata)

>>> with open('mydata.pickle','rb') as myrestoredata:
	a_list=pickle.load(myrestoredata)
	
>>> with open('mydata.pickle','wb') as mysavedata:
	pickle.dump([1,2,'three'], mysavedata)

>>> print (a_list)
[1, 2, 'three']
>>> with open('mydata.pickle','rb') as pickdata:
	print pickdata.read()

(lp0
I1
aI2
aS'three'
p1
a.
>>> with open('mydata.pickle','rb') as myrestoredata:
	a_list=pickle.load(myrestoredata)
	print myrestoredata.read()
	print a_list

	

[1, 2, 'three']
>>> with open('mydata.pickle','rb') as myrestoredata:
	a_list=pickle.load(myrestoredata)
	print myrestoredata.read()

#多个文件同时打开
with open('man.txt','w') as m_f, open('woman.txt','w') as wof:
	print(m_f.read())
    print(wof.read())
```



### 11，排序

sort(), sorted() BIF都会按升序对数据进行排序

要降序排序，需要向sort(), sorted()传入参数reverse=True

### 11.1, 正则

```python

#查找一个开始"(",后面是3个数字，然后是一个结束")"
'\((\d{3})\)'
```

概述 

```python
全称 Regular Expression,  一种文本模式，搜索文本时要匹配的一个或多个字符串

常见场景：数据验证， 文本扫描， 文本提取，文本替换，文本分割

```



语法：

```python
字面值， 普通字符， 需转义(\ ^ $ . |? * +)

```



匹配：

```python
元字符,单字预定义元字符， . 除\n外的所有字符

 \d 数字，等同于[0-9]

\D 非数字，等同于[^0-9]

\s    空白字符  \t\n\r\f\v

\S  非空白字符[^\t\n\r\f\v]

\w 字母数字字符 [a-zA-Z0-9]

\W  非字线数字 [^a-zA-Z0-9]


批量备选  |yes|no


量词(字符，元字符，字符集如何重复) 


? 0|1次 ， *  0或多次  + 1或多次， 

特定： {n,m}范围次数， {n} n次， {n,}至少n次


贪婪(默认):尽量匹配最大范围
非贪婪：  尽量匹配最小范围结果
	方法， 匹配后面加量词
     ??, *?, +?

边界匹配：^  行首， $ 行尾 , \b, \B

特殊符号与字符

```



正则 RegexObject

```python
模式对象    表现编译后的对象
编译一个模式   re.compile(r'<html>')
.findall(查找所有非重叠匹配项)，返回list

pattern.match(string[,pos[,endpos]])  从起始位置开始匹配，返回MatchObject

pattern.findall(text)
p1 = re.compile(r'd+')
                
pattern.search()
p2= re.compile(r'[A-Z]\w+')
                
pattern.finditer()   
	查找所有匹配项，返回一个MatchObject元素的迭代对象
p_name = 
```



正则模式 MatchObject

```python
表现被匹配的模式
.group()   整个分组
	参数为0或空返回整个匹配
    有参数时返回特定分组匹配细节
    参数也可以是分组名称
.groups()   值形成的分组
	返回包含所有子分组的元组
.start()  返回特定分组的起始索引
.end()  返回特定分组的终止索引
.span()  返回特定分组的起至索引元组
.groupdict()   以字典表形式返回分组名及结果

text = 'Peter is 19 years Tom is 21 years'
pattern = re.compile(r'\d+')
pattern.search（text）
```



Group编组

```python
场景：
	从匹配模式中提取信息
    创建子正则以应用量词
    限制备选范围
    重用正则模式提取的内容
声明：    
	(模式)
    (?P<name>模式)
   
引用：
	匹配对象内 m.group('name')
    模式内 (?P=name)
    表现内  \g<name>

分组  ()， 如： (.*?), r'(\d+).*?(+d\)'

re.search(r'ab','ababc')

```





综合应用, 字符处理

```python
test = 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex'

字符操作
re.split(string, maxsplit=0)   分割字符串
re.sub(repl, string, count=0) 替换指定字符串
re.subn(repl, string, count=0) 替换并返回替换的数量

编译标记
	改变正则默认行为  
    忽略大小写，re.I, 
    匹配多行 re.M
    指定.， 匹配所有字符包括\n  re.S
    
    
 	清理正则缓存  re.purge()
	逃逸字符  re.escape('^')   不考虑 ^ 的正则意义
```





### 12，集合，删除重复项

```python
#集合会自动忽略重复的数据项
>>> dis = set()
>>> dis
set([])
>>> type(dis)
<type 'set'>
>>> dis = {1.2,33,21.1,1.2,"one",7}
>>> dis
set([33, 7, 1.2, 21.1, 'one'])

#添加列表值到集合
>>> lis6=[12,21,22,11,12,23]  #列表有重复值12
>>> dis2=set()       #建立空集合
>>> for item in lis6:  
	dis2.add(item)   #添加集合

>>> dis2
set([11, 12, 21, 22, 23])
```



### 13  ipython

-  安装ipykernel，用于交互式绘图

   ```python
   python -m pip install ipykernel
   ```
#需要vc++ for python27 
building '_scandir' extension
error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
#成功安装
Successfully installed backports.shutil-get-terminal-size-1.0.0 colorama-0.3.9 ipykernel-4.6.1 ipython-5.3.0 pathlib2-2.2.1 pickleshare-0.7.4 prompt-toolkit-1.0
.14 pygments-2.2.0 scandir-1.5 simplegeneric-0.8.1 wcwidth-0.1.7 win-unicode-console-0.5
#安装Python 2 ketnel 
python  -m ipykernel install --user
Installed kernelspec python2 in C:\Users\wb-xyd261196\AppData\Roaming\jupyter\kernels\python2

#查看工具配置
C:\>jupyter --paths
config:
    C:\Users\wb-xyd261196\.jupyter
    c:\python27\etc\jupyter
    C:\ProgramData\jupyter
data:
    C:\Users\wb-xyd261196\AppData\Roaming\jupyter
    c:\python27\share\jupyter
    C:\ProgramData\jupyter
runtime:
    C:\Users\wb-xyd261196\AppData\Roaming\jupyter\runtime




### 14 变量与存储

```pyton
变量：对象别名
类型：
	描述数据形态及支持操作
	python动态类型  --变量无类型约束
	               --类型取决于关联对象
存储：	               
	1，对象有类型，存储在内存区域
	2，变量名指向实际对象。变量本身无类型
	3，对象本身带有类型描述及引用计数器
	4，共享引用：多个变量引用同一对象  --  == 引用对象字面值是否相同
									--  is 对象的值和地址是否都相同
									    id（）检查对象地址
									    短字符串也可能被缓存
									    0-255 Python自动缓存
>>> a = 45
>>> b = 45
>>> a ==b
True
>>> a is b
True
>>> c =445
>>> d =445
>>> c ==d
True
>>> c is d
False
									   
    
 


```





### 15 垃圾回收机制

```python

垃圾回收机制：
	1.python自动释放未被引用的对象
	2.通过对象引用计数器统计引用
	
```



### 16 内置常用数据类型

```python
1, 数值类型  -- 整型int|浮点float -- 字面值 -0o八进制 0x 十六进制 0b 二进制           
   			 >>> 0o9 SyntaxError: invalid token  >>> 0o7  7
             >>> 0x1234  4660   >>> 0x169  361 >>> 0xf 15
             >>> 0b010101001  169

	1.1 常用函数
        转换int>>>int("177", 8)  127   >>>int('177', 16)  375
        16进制转换:hex(10)  '0xa'
        8进制转换:oct(10)  '012'
        2进制转换:bin(10)  '0b1010'
     1.2 常用工具 -math
        (地板)去掉小数部分坐标左方
        math.floor(3.99)   3
        math.floor(-3.14)  -4
        (天花板)向上取整
        math.ceil(3.14)  4
        math.ceil(-3.14) -3
        往0的方向截取截断
        math.trunc(3.99)   3
        math.trunc(-3.14)  -3
        四舍五入
        round(3.14)   3
        round(3.95)
        math.pi  3.1415...
        math.sin(12) -0.5365729180004349
      1.3 浮点精度处理类 devimal
         from devimal import Decimal
         格式化 format
      1.4 
        
2，序列 list  -- 可变长度，异质，可任意嵌套
             --支持原位改变
             -- 对象引用数组
3，集合
4，映射
5，程序单元类型
6，其他  -- 类型对象   type(obj)
             
		-- 空对象    None  （默认缓存好的）
        -- 布尔      bool  --True， Flase （默认缓存好的）本质是 1，0
        >>> x = 5 + True  >>> x   6
        >>> y = 5 + False >>> y   5
 
```

 

### 17，函数工具

map(func, sc)  作用于一个可迭代对象，做一些操作，返回一个可迭代对象

```python
sc = [12,3,123,1,23,123,12,3]
def func(x):
	return x + 2
result = map(func, sc)  #result 为一个可迭代对象
lisrest = list(map(func, sc))
map(func, sc)
[14, 5, 125, 3, 25, 125, 14, 5]

#map + lambda
lambda s:s+2, sc
(<function <lambda> at 0x00000000031C1048>, [12, 3, 123, 1, 23, 123, 12, 3])
>>> map(lambda s:s+2, sc)
[14, 5, 125, 3, 25, 125, 14, 5]
>>> type(map(lambda s:s+2, sc))
<type 'list'>
# 将列表字符串大写并返回
stud = ["Tom", 'Jerry', 'Madr']
map(lambda s:s.upper(), stud)
['TOM', 'JERRY', 'MADR']
```

filter (func,  iterable)  过滤选择项

```python
平常做法
sc = [12,3,123,1,23,124,12,3]
def func2(x):
	return x >=60
filter(func2, sc)
[123, 124]

# lambda 找出含e的元素
stud = ["Tom", 'Jerry', 'Madr']
resu = filter(lambda n:'e' in n, stud)
>>> print resu
['Jerry']

```

reduce  合并减少

```python
scores = [55,34,123,91,23,124,12,38]

#自写函数
>>> for s in scores[1:]:
	res += s	
>>> print res
500
#sum操作
>>> print sum(scores)  #两两合并
500

#reduce
import functools
>>> def fund(x,y):
	return x + y
>>> print(functools.reduce(fund, scores))
500

#lambda 表达式
print(functools.reduce(lambda x,y:x + y, scores))
500

print(functools.reduce(lambda x,y:x * y, scores))
27220899625920

#operator
functools.reduce(operator.add, scores)
500
>>> functools.reduce(operator.mul, scores)
27220899625920L
```



### 18 类间关系 

```python

依赖，关联与聚合， 继承与多态
```



### 19, 迭代

```python
迭代工具  for  i in list
iter()   __iter__()   迭代函数  返回一个可迭代对象
next()   __next__()   迭代方法
```

```python
scores = [85,32,123,321,223]
[x for x in scores if x >=160]
#推导大于160的成员
321,223
#推导含e的成员
students = ['Tom', 'Jerry', 'Mike']
[n for n in students if 'e' in n]

sc = [32,32,123,321,322]
#提取对象
[s for s in sc]
[32,32,123,321,322]
#去除重复
{s for s in sc}
{32,123,321,322}

```



### 20 lambda

```python

map(lambda x:x+2, lis1)
[3, 4, 5]

reduce  合并
filter 
```



### 21, ASCII, UTF8 字符集处理

用处， 在网络传输需要encode，收到后需要decode

**概述**

```python
字符串， 字节， 字符类型 转换
bytes 手动声明  b''
字符串编码 str.encode()
构造函数  bytes()

bytearray
```



字符编码

```python
ASCII: 存储1Byte, 0-127
latin-1: 存储1Byte, 128-255 # 拉丁
UTF-8: 可变字节  0-127， 使用单字节， 128-2047 双字节存储， > 2047  3-4 Byte
       每Byte使用128-255
UTF-16：2 Byte存储字符（另加2Byte作为标识）
UTF-32：4 Byte

```

内置函数

```python
ord() 获取字符代码点
chr() 获取代码点对应字符
str.encode('编码')  将特定字符编码
bytes.decode('编码')  将字符编码解码为字符文本
```

BOM处理

```python
open('data.txt', 'w|r', encoding='utf-8-sig')
```



### 22, 多线程 threading

-  _thread 模块使用锁的方式管理并发线程, 性能不如threading
- threading  
- threading.current_thread().name   获取线程名称
- 同步原语-锁  
-  lock = threading.Lock()
-  lock.acquire()  获得锁
-  lock.release() 释放锁
-  with  lock:   #上下文操作, 不用上面两个锁的操作
  -  for i in threads: 
    - i.start()



### multiprocessing 模块

计算密集型使用此模块



### concurrent.futures 应用



