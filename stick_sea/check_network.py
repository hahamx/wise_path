# -*- coding:utf-8 -*-
import os, sys, re
import subprocess

num = int(input('Enter an Integer:'))
# ip=str(input('Enter ip:'))
for i in range(68, 70):
    ret = subprocess.check_call('ping 192.168.11.%d -n %d ' % (i, num), shell=True,
                                stdout=open(r'D:\test_case\iptmp.txt', 'w'), stderr=subprocess.STDOUT)

    if ret == 0:
        print ("%d: is alive" % i)
    else:
        print ("%d is down" % i)