#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :client.py
# Date      :2024.11.02
# Time      :16:40
# Author    :Sun Chang long
# Email     :1204403199@qq.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.98.105", 2200)
client.sendto("hello".encode("UTF-8"), addr)
data, _ = client.recvfrom(1024)
print(data)
client.close()
