#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :server.py
# Date      :2024.11.02
# Time      :16:36
# Author    :Sun Chang long
# Email     :1204403199@qq.com

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.98.105", 2200)
server.bind(addr)
data, client_addr = server.recvfrom(1024)
print(data)
print(client_addr)
server.sendto("ni hao".encode("utf-8"), client_addr)
server.close()
