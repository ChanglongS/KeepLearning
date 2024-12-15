#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :file_server.py
# Date      :2024.11.07
# Time      :21:35
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

import socket
import sys
import struct


def tcp_init():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    addr = ("192.168.212.105", 2000)
    s.bind(addr)
    s.listen(5)
    return s


def send_file():
    s = tcp_init()
    new_client, client_addr = s.accept()
    file_name = 'file'
    file_name_bytes = file_name.encode("utf-8")
    train_head_bytes = struct.pack("I", len(file_name_bytes))
    new_client.send(train_head_bytes + file_name_bytes)

    f = open(file_name, "rb")
    file_content_bytes = f.read()
    train_head_bytes = struct.pack("I", len(file_content_bytes))
    new_client.send(train_head_bytes + file_content_bytes)

    f.close()
    new_client.close()
    s.close()


if __name__ == '__main__':
    send_file()
