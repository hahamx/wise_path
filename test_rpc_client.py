# -*- coding:utf-8 -*-

import threading
import struct
import json
import socket
"""
socket
client:
sock = socket.socket()
sock.connect()
sock.read()
sock.write()
sock.close()
server:
sock = socket.socket()
sock.bind()  #绑定端口
sock.listen() 
sock.accept()
sock.close()

"""

"""
struct:
value_in_bytes = struct.pack('I',1024) #将一个整数编码成 4 个字节的字符串
value, = struct.unpack("I", value_in_bytes)#将一个 4 字节的字符串解码成一个整数
# 注意等号前面有个逗号，这个非常重要，它不是笔误。
# 因为 unpack 返回的是一个列表，它可以将一个很长的字节串解码成一系列的对象。
# value 取这个列表的第一个对象。
"""

"""
json:
raw = json.dumps({"hi":"world"}) 
pp = json.loads(raw)

"""


"""
# 消息协议, 确定消息边界, 约定长度法
# 我们将请求和响应使用 json 序列化成字符串作为消息体，然后通过 Python 内置的 struct 包将消息体的长度整数转成 4 个字节的长度前缀字符串。

// 输入
{
in: "ping"
params:"ireader e"
}

// 输出
{
out: "pong"
result: "ireader e"
}
"""
# coding: utf-8
# client.py

import json
import time
import struct
import socket


def rpc(sock, in_, params):
    response = json.dumps({"in": in_, "params": params})  # 请求消息体
    length_prefix = struct.pack("I", len(response)) # 请求长度前缀
    sock.send(length_prefix)
    sock.sendall(response)  # sendall = send + flush
    length_prefix = sock.recv(4)  # 响应长度前缀
    length, = struct.unpack("I", length_prefix)
    body = sock.recv(length) # 响应消息体
    response = json.loads(body)
    return response["out"], response["result"]  # 返回响应类型和结果

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8080))
    for i in range(10): # 连续发送 10 个 rpc 请求
        out, result = rpc(s, "ping", "ireader %d" % i)
        print(out, result)
        time.sleep(1)  # 休眠 1s，便于观察
    s.close() # 关闭连接...

