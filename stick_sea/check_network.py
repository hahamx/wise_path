# -*- coding:utf-8 -*-
import os
import sys
import re
import subprocess
import commands

#if os.system()
(sta, out) = commands.getstatusoutput("ipconfig /allcompartments")
cmd = "ipconfig /allcompartments"
p1 = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
(our2, err) = p1.communicate()
out1 = """
Windows IP 配置


==============================================================================
分段 1 的网络信息(活动)
==============================================================================

以太网适配器 本地连接:

   媒体状态  . . . . . . . . . . . . : 媒体已断开
   连接特定的 DNS 后缀 . . . . . . . :

无线局域网适配器 无线网络连接:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::4c17:b09a:9f5f:8d8d%12
   IPv4 地址 . . . . . . . . . . . . : 192.168.0.103
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . : 192.168.0.1

以太网适配器 VMware Network Adapter VMnet1:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::5500:193:a154:1f45%15
   自动配置 IPv4 地址  . . . . . . . : 169.254.31.69
   子网掩码  . . . . . . . . . . . . : 255.255.0.0
   默认网关. . . . . . . . . . . . . :
"""
ip_list = []
# with open('s.txt', 'ab') as sf:
#    sf.write(str(out1))

# with open('s.txt', 'r+') as s1f:
#     lines = s1f.readlines()
#     for line in lines:
#         if "IPv4" in str(line):
#             print 'line', line
#             lis = str(line).split(':')
#             print 'lis', lis, lis[1]
#             ip_list.append(lis[1])
#         else:
#             continue
# print ip_list


ips = []
print our2.encode("ascii").decode("utf8")
print "out", our2.encode("utf8")
for line in our2:
    if "IPv4" in str(line):
        print 'line', line
        lis = str(line).split(':')
        print 'lis', lis, lis[1]
        ips.append(lis[1])
    else:
        continue
print ips