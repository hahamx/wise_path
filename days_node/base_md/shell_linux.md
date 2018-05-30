1，服务后台程序，daemon， 有stand alone(服务在/etc/init.d/*目录)，super daemon（/etc/xinetd.d）两种， 变更相关端口需要更改 /etc/services文件,重新启动 /etc/init.d/xinetd

2，程序安装，RPM，Tarball工具 ，查找命令：locate，find，which，如： locate httpd.conf
  （Tarball安装服务器软件一般是二进制的，没有shell脚本启动，关闭，重新读取设置信息）
3，解压缩命令：tar ,gzip,bzip,compress

4,调试工具命令  gdb
 
安全性：
1，修改/etc/login.defs文件规则，使用户半年更换一次密码
2，/etc/security/limits.conf 规范用户权限
3，利用pam模块额外进行密码验证工作
4，修改/etc/hosts.allow 及/etc/hosts.deny限制相关ip网段，网域
5，netfilter防火墙，iptables配置单机防火墙，如果linux的 kernel是 2.4版本以上的，防火墙机制是iptables
6，日志，/etc/syslog.conf 配置日志信息，一般日志会保存在/var/log中

25个常用命令
1，ls
“ls -l”命令以详情模式(long listing fashion)列出文件夹的内容。
"ls -a"命令会列出文件夹里的所有内容，包括以"."开头的隐藏文件。
2，lsblk   (或者tree)
"lsblk"就是列出块设备。除了RAM外，以标准的树状输出格式，整齐地显示块设备。
“lsblk -l”命令以列表格式显示块设备(而不是树状格式)。
注意：lsblk是最有用和最简单的方式来了解新插入的USB设备的名字，特别是当你在终端上处理磁盘/块设备时
3， md5sum命令
“md5sum”就是计算和检验MD5信息签名。md5 checksum(通常叫做哈希)使用匹配或者验证文件的文件的完整性，因为文件可能因为传输错误，磁盘错误或者无恶意的干扰等原因而发生改变。
例如：
root@tecmint:~# md5sum teamviewer_linux.deb
 
47790ed345a7b7970fc1f2ac50c97002  teamviewer_linux.deb
注意：用户可以使用官方提供的和md5sum生成签名信息匹对以此检测文件是否改变。Md5sum没有sha1sum安全 。
4，dd命令
“dd”命令代表了转换和复制文件。可以用来转换和复制文件，大多数时间是用来复制iso文件(或任何其它文件)到一个usb设备(或任何其它地方)中去，所以可以用来制作USB启动器。
root@tecmint:~# dd if=/home/user/Downloads/debian.iso of=/dev/sdb1 bs=512M; sync
注意：在上面的例子中，usb设备就是sdb1（你应该使用lsblk命令验证它，否则你会重写你的磁盘或者系统），请慎重使用磁盘的名，切忌。
dd 命令在执行中会根据文件的大小和类型 以及 usb设备的读写速度，消耗几秒到几分钟不等。
5，unname
"uname"命令就是Unix Name的简写。显示机器名，操作系统和内核的详细信息
1
2
3
root@tecmint:~# uname -a
 
Linux tecmint 3.8.0-19-generic #30-Ubuntu SMP Wed May 1 16:36:13 UTC 2013 i686 i686 i686 GNU/Linux
注意： uname显示内核类别， uname -a显示详细信息。上面的输出详细说明了uname -a
“Linux“: 机器的内核名
“tecmint“: 机器的节点名
“3.8.0-19-generic“: 内核发布版本
“#30-Ubuntu SMP“: 内核版本
“i686“: 处理器架构
“GNU/Linux“: 操作系统名

6，history
history显示在终端中执行过的所有命令和历史
root@tecmint:~# history
 
 1  sudoadd-apt-repository ppa:tualatrix/ppa
 2  sudoapt-get update
 9  sudoapt-get installmy-weather-indicator
 10 pwd
 11 cd&& sudocp-r unity/6/usr/share/unity/

注意：按住“CTRL + R”就可以搜索已经执行过的命令，它可以在你写命令时自动补全。
1
(reverse-i-search)`if': ifconfig
7，sudo
“sudo”(super user do)命令允许授权用户执行超级用户或者其它用户的命令。通过在sudoers列表的安全策略来指定。
1
root@tecmint:~# sudo add-apt-repository ppa:tualatrix/ppa
注意：sudo 允许用户借用超级用户的权限，然而"su"命令实际上是允许用户以超级用户登录。所以sudo比su更安全。
并不建议使用sudo或者su来处理日常用途，因为它可能导致严重的错误如果你意外的做错了事，这就是为什么在linux社区流行一句话：
“To err is human, but to really foul up everything, you need root password.”
“人非圣贤孰能无过，但是拥有root密码就真的万劫不复了。” # 译

8，mkdir
“mkdir”(Make directory)命令在命名路径下创建新的目录。然而如果目录已经存在了，那么它就会返回一个错误信息"不能创建文件夹，文件夹已经存在了"("cannot create folder, folder already exists")
mkdir：不能创建目录`tecmint`，因为文件已经存在了。（上面的输出中不要被文件迷惑了，你应该记住我开头所说的-在linux中，文件，文件夹，驱动，命令，脚本都视为文件）
9，touch命令
“touch”命令代表了将文件的访问和修改时间更新为当前时间。touch命令只会在文件不存在的时候才会创建它。如果文件已经存在了，它会更新时间戳，但是并不会改变文件的内容。
1
root@tecmint:~# touch tecmintfile
注意：touch 可以用来在用户拥有写权限的目录下创建不存在的文件。

10，chmod命令
chmod更改文件的模式位，文件中存在三种类型的权限，  
Read（r）=4
Write（w）=2
 Execute（x）=1 
另外还可以对3种用户和用户组分配权限，第一个（即前3位）为拥有者，然后中间为用户所在组，最后是其他用户
rwxr-x--x   aaa.sh
这里拥有者为读写执行权限，用户所属组为读和执行权限，其他用户为执行权限
改变他为所有用户都有读写执行权限
chmod 777 aaa.sh
改变他为所有用户为读写权限
chmod 666 aaa.sh
拥有着有全部权限，其他用户只有执行权限
chmod 711 aaa.sh
注意：对于系统管理员和用户来说，这个命令是最有用的命令之一了。在多用户环境或者服务器上，对于某个用户，如果设置了文件不可访问，那么这个命令就可以解决，如果设置了错误的权限，那么也就提供了为授权的访问。
11,chown命令
“chown”命令就是改变文件拥有者和所在用户组。每个文件都属于一个用户组和一个用户。在你的目录下，使用"ls -l",你就会看到像这样的东西。
1
2
3
4
root@tecmint:~# ls -l
 
drwxr-xr-x 3 server root4096 May 10 11:14 Binary
drwxr-xr-x 2 server server 4096 May 13 09:42 Desktop
在这里，目录Binary属于用户"server",和用户组"root",而目录"Desktop"属
在这里，目录Binary属于用户"server",和用户组"root",而目录"Desktop"属于用户“server”和用户组"server"
“chown”命令用来改变文件的所有权，所以仅仅用来管理和提供文件的用户和用户组授权。
1
2
3
4
root@tecmint:~# chown server:server Binary
 
drwxr-xr-x 3 server server 4096 May 10 11:14 Binary
drwxr-xr-x 2 server server 4096 May 13 09:42 Desktop
注意：“chown”所给的文件改变用户和组的所有权到新的拥有者或者已经存在的用户或者用户组。

12，apt命令
Debian系列以“apt”命令为基础，“apt”代表了Advanced Package Tool。APT是一个为Debian系列系统（Ubuntu，Kubuntu等等）开发的高级包管理器，在Gnu/Linux系统上，它会为包自动地，智能地搜索，安装，升级以及解决依赖。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
root@tecmint:~# apt-get install mplayer
 
Reading package lists... Done
Building dependency tree      
Reading state information... Done
The following package was automatically installed and is no longer required:
  java-wrappers
Use 'apt-get autoremove'to remove it.
The following extra packages will be installed:
  esound-common libaudiofile1 libesd0 libopenal-data libopenal1 libsvga1 libvdpau1 libxvidcore4
Suggested packages:
  pulseaudio-esound-compat libroar-compat2 nvidia-vdpau-driver vdpau-driver mplayer-doc netselect fping
The following NEW packages will be installed:
  esound-common libaudiofile1 libesd0 libopenal-data libopenal1 libsvga1 libvdpau1 libxvidcore4 mplayer
0 upgraded, 9 newly installed, 0 to remove and 8 not upgraded.
Need to get 3,567 kB of archives.
After this operation, 7,772 kB of additional disk space will be used.
Do you want to continue[Y/n]? y

1
2
3
4
5
6
7
8
9
10
11
12
13
14
root@tecmint:~# apt-get update
Hit http://ppa.launchpad.net raring Release.gpg                                          
Hit http://ppa.launchpad.net raring Release.gpg                                          
Hit http://ppa.launchpad.net raring Release.gpg                     
Hit http://ppa.launchpad.net raring Release.gpg                     
Get:1 http://security.ubuntu.com raring-security Release.gpg [933 B]
Hit http://in.archive.ubuntu.com raring Release.gpg                                                  
Hit http://ppa.launchpad.net raring Release.gpg                     
Get:2 http://security.ubuntu.com raring-security Release [40.8 kB]  
Ign http://ppa.launchpad.net raring Release.gpg                                                 
Get:3 http://in.archive.ubuntu.com raring-updates Release.gpg [933 B]                           
Hit http://ppa.launchpad.net raring Release.gpg                                                               
Hit http://in.archive.ubuntu.com raring-backports Release.gpg
注意：上面的命令会导致系统整体的改变，所以需要root密码（查看提示符为"#"，而不是“$”）.和yum命令相比，Apt更高级和智能。
见名知义，apt-cache用来搜索包中是否包含子包mplayer, apt-get用来安装，升级所有的已安装的包到最新版。
关于apt-get 和 apt-cache命令更多信息，

13，tar命令
“tar”命令是磁带归档(Tape Archive)，对创建一些文件的的归档和它们的解压很有用。
1
root@tecmint:~# tar -zxvf abc.tar.gz (记住'z'代表了.tar.gz)

1
root@tecmint:~# tar -jxvf abc.tar.bz2 (记住'j'代表了.tar.bz2)

1
root@tecmint:~# tar -cvf archieve.tar.gz(.bz2) /path/to/folder/abc
注意： "tar.gz"代表了使用gzip归档，“bar.bz2”使用bzip压缩的，它压缩的更好但是也更慢。
14，cal
 用来显示现在或过去未来的时间日期
显示现在的时间    cal
显示过去1970年2月的时间    cal 02 1970
显示未来2245年2月的时间  cal  02 2245
最小显示单位为月。
15，date

“date”命令使用标准的输出打印当前的日期和时间，也可以深入设置

date --set='14 may 2013 13:57'
注意：这个命令在脚本中十分有用，以及基于时间和日期的脚本更完美。而且在终端中改变日期和时间，让你更专业！！！（当然你需要root权限才能操作这个，因为它是系统整体改变）
16，cat命令
“cat”代表了连结（Concatenation），连接两个或者更多文本文件或者以标准输出形式打印文件的内容。
cat a.txt b.txt c.txt d.txt>>abcd.txt
cat abcd.txt
注意：“>>”和“>”调用了追加符号。它们用来追加到文件里，而不是显示在标准输出上。“>”符号会删除已存在的文件，然后创建一个新的文件。所以因为安全的原因，建议使用“>>”，它会写入到文件中，而不是覆盖或者删除。
通配符是shell的特色，和任何GUI文件管理器相比，它使命令行更强大有力！
这里就是常用通配符列表：
1
2
3
4
5
6
7
8
Wildcard Matches
   *            零个或者更多字符
   ?            恰好一个字符
[abcde]             恰好列举中的一个字符
 [a-e]          恰好在所给范围中的一个字符
[!abcde]        任何字符都不在列举中
[!a-e]          任何字符都不在所给的范围中
{debian,linux}      恰好在所给选项中的一整个单词
! 叫做非，带'！'的反向字符串为真
（more可分页显示）
17,cp
“copy”就是复制。它会从一个地方复制一个文件到另外一个地方。
注意： cp，在shell脚本中是最常用的一个命令，而且它可以使用通配符（在前面一块中有所描述），来定制所需的文件的复制。

18,mv
“mv”命令将一个地方的文件移动到另外一个地方去。
注意：mv 命令可以使用通配符。mv需谨慎使用，因为移动系统的或者未授权的文件不但会导致安全性问题，而且可能系统崩溃。
19,pwd
pwd”（print working directory），在终端中显示当前工作目录的全路径。
20,cd
最后，经常使用的“cd”命令代表了改变目录。它在终端中改变工作目录来执行，复制，移动，读，写等等操作。
注意： 在终端中切换目录时，cd就大显身手了。“cd ～”会改变工作目录为用户的家目录，而且当用户发现自己在终端中迷失了路径时，非常有用。“cd ..”从当前工作目录切换到(当前工作目录的)父目录。

21，ps，top
http://blog.chinaunix.net/uid-28253945-id-3432998.html
ps 会显示所有状态的进程信息，加管道符可以过滤需要看见的进程
top 会实时的显示正在运行的进程信息 
ps  -eLo pid,lwp,pcpu | grep  21760   查看该进程下所有线程的状态
gstack PID
cpu 占用率高的线程找出来:
ps H -eo user,pid,ppid,tid,time,%cpu,cmd--sort=%cpu

多核，top后按大键盘1看看，可以显示每个cpu的使用率
22，kill
用于终止进程的执行，后面可跟不同的参数

23，grep
cd /alidata/backup/tomcat_log_backup/2016-11-30/ZongHePingTai04_165/10.117.37.193 
 grep -A 10 20161130230109  miyadate.log 
24,改变文件编码方式 用Vim
 :set fileencoding=utf-8
 :set fileencoding=ISO-8859
enconv -L zh_CN -x UTF-8 filename
 查看文件编码file命令
file ip.txt  ip.txt: UTF-8 Unicode text, with escape sequences
比如将一个UTF-8 编码的文件转换成GBK编码update.txt
iconv -f GBK -t UTF-8   -o update.txt
25 正则表达式
只有掌握了正则表达式，才能全面地掌握 Linux 下的常用文本工具（例如：grep、egrep、GUN sed、 Awk 等） 的用法
    grep 与 egrep 正则匹配文件，处理文件方法
grep 指令后不跟任何参数，则表示要使用 ”BREs“ 
grep 指令后跟 ”-E" 参数，则表示要使用 “EREs“
grep 指令后跟 “-P" 参数，则表示要使用 “PREs"
a. grep 与 egrep 的处理对象：文本文件
b. grep 与 egrep 的处理过程：查找文本文件中是否含要查找的 “关键字”（关键字可以是正则表达式） ，如果含有要查找的 ”关健字“，那么默认返回该文本文件中包含该”关健字“的该行的内容，并在标准输出中显示出来，除非使用了“>" 重定向符号,
c. grep 与 egrep 在处理文本文件时，是按行处理的
sed 功能与作用
sed 命令参数 “-r ” ，则表示要使用“EREs"
a. sed 处理的对象：文本文件
b. sed 处理操作：对文本文件的内容进行 --- 查找、替换、删除、增加等操作
c. sed 在处理文本文件的时候，也是按行处理的
Awk（gawk）正则表达式特点
1）Awk 文本工具支持：EREs
awk 指令默认是使用 “EREs"
2）Awk 文本工具处理文本的特点
a. awk 处理的对象：文本文件
b. awk 处理操作：主要是对列进行操作
注意： 当使用 BERs（基本正则表达式）时，必须在下列这些符号前加上转义字符（'\'），屏蔽掉它们的 speical meaning  “?,+,|,{,},（,）” 这些字符，需要加入转义符号”\”
 
注意：修饰符用在正则表达式结尾，例如：/dog/i，其中 “ i “ 就是修饰符，它代表的含义就是：匹配时不区分大小写，那么修饰符有哪些呢？常见的修饰符如下:
g   全局匹配（即：一行上的每个出现，而不只是一行上的第一个出现）
s    把整个匹配串当作一行处理
m    多行匹配
i    忽略大小写
x    允许注释和空格的出现
U    非贪婪匹配


tcp连接端口数可超过65535

理论

系统通过一个四元组来唯一标识一条TCP连接. 这个四元组的结构是{local ip, local port, remote ip, remote port}, 对于IPv4, 系统理论上最多可以管理2^(32+16+32+16), 2的96次方个连接. 如果不仅仅考虑TCP, 则是一个五元组, 加上协议号(TCP, UDP或者其它).
实践

服务器绑定一个ip:port, 然后accept连接, 所有accept的连接使用的本地地址也是同样的ip:port.
cat /proc/sys/net/ipv4/ip_local_port_range    客户端主动连接发起连接，本地端口使用范围
cat /proc/sys/fs/file-max 580382    系统支持的最大打开文件描述符数(包括socket连接)
ulimit -n 1024     单个进程所能打开的最大文件描述符数
修改本地字符集
