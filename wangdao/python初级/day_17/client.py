#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :client.py
# Date      :2024.11.07
# Time      :10:15
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from socket import *
import select
import sys


def tcp_client():
    if len(sys.argv) < 2:
        return
    client = socket(AF_INET, SOCK_STREAM)
    addr = (sys.argv[1], 2000)
    client.connect(addr)
    epoll = select.epoll()
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == client.fileno():
                data = client.recv(1024)
                if data:
                    print(data.decode("utf-8"))
                else:
                    print("de connect!")
                    return
            elif fd == sys.stdin.fileno():
                data = input()
                client.send(data.encode("utf-8"))

    client.close()


if __name__ == '__main__':
    tcp_client()
