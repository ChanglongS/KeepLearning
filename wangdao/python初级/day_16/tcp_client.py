#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :tcp_client.py
# Date      :2024.11.05
# Time      :13:15
# Author    :Sun Chang long
# Email     :1204403199@qq.com

import socket


def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.212.105", 2000))
    client.send("how are you".encode("utf-8"))
    data = client.recv(5)
    print(data.decode("utf-8"))
    data = client.recv(5)
    print(data.decode("utf-8"))
    client.close()


if __name__ == '__main__':
    tcp_client()
