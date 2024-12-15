#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :tcp_server.py
# Date      :2024.11.05
# Time      :11:48
# Author    :Sun Chang long
# Email     :1204403199@qq.com

import socket


def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.212.105", 2000)
    s.bind(addr)
    s.listen(5)
    new_client, client_addr = s.accept()
    print(client_addr)
    data = new_client.recv(100)
    print(data.decode("utf-8"))
    new_client.send("hello,world".encode("utf-8"))
    new_client.close()
    s.close()


if __name__ == '__main__':
    tcp_server()
