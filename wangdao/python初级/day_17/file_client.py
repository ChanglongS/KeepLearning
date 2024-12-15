#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :file_client.py
# Date      :2024.11.07
# Time      :21:35
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from socket import *
import sys
import struct


def file_client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.212.105', 2000))

    train_head_bytes = client.recv(4)
    file_name_tuple = struct.unpack('I', train_head_bytes)
    file_name = client.recv(file_name_tuple[0])
    f = open(file_name.decode("uft-8"), 'wb')

    train_head_bytes = client.recv(4)
    file_content_tuple = struct.unpack('I', train_head_bytes)
    file_content = client.recv(file_content_tuple[0])
    f.write(file_content)

    f.close()
    client.close()


if __name__ == '__main__':
    file_client()
