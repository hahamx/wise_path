# coding: utf8
# blocking_single.py

import json
import struct
import socket
import threading
import os


def handle_conn(conn, addr, handlers):
    print("{},comes".format(addr))
    while True:  # 循环读写
        length_prefix = conn.recv(4)  # 请求长度前缀
        if not length_prefix:  # 连接关闭了
            print("{}, bye".format(addr))
            conn.close()
            break  # 退出循环，处理下一个连接
        length, = struct.unpack("I", length_prefix)
        body = conn.recv(length)  # 请求消息体
        request = json.loads(body)
        in_ = request['in']
        params = request['params']
        print (in_, params)
        handler = handlers[in_]  # 查找请求处理器
        handler(conn, params)  # 处理请求


def loop(sock, handlers):
    while True:
        conn, addr = sock.accept()  # 接收连接
        # handle_conn(conn, addr, handlers)  # 单线程处理连接
        # threading._start_new_thread(handle_conn, (conn, addr, handlers))
        # 多线程处理
        pid = os.fork() # 创建子进程处理
        if pid < 0: # fork error
            return
        if pid > 0: # parent process
            conn.close() # 关闭父进程client套接字
            continue
        if pid == 0:
            sock.close()  # 关闭子进程服务器套接字
            handle_conn(conn, addr, handlers)
            break  # 处理完成后一定退出循环, 不然子进程也继续accept链接


def ping(conn, params):
    send_result(conn, "pong", params)


def send_result(conn, out, result):
    response = json.dumps({"out": out, "result": result})  # 响应消息体
    length_prefix = struct.pack("I", len(response))  # 响应长度前缀
    conn.send(length_prefix)
    conn.sendall(response)  # sendall = send + flush


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个 TCP 套接字
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 打开 reuse addr 选项
    sock.bind(("localhost", 8080)) # 绑定端口
    sock.listen(1)  # 监听客户端连接

    handlers = {  # 注册请求处理器
        "ping": ping
    }
    print("start server 8080...")
    loop(sock, handlers)  # 进入服务循环...

