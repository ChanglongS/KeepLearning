#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :server.py
# Date      :2024.11.07
# Time      :10:15
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com


from socket import *
import sys
import select


def tcp_server():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ("", 2000)
    s.bind(addr)
    s.listen(5)
    new_client, client_addr = s.accept()
    epoll = select.epoll()
    epoll.register(new_client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == new_client.fileno():
                data = new_client.recv(1024)
                if data:
                    print(data.decode("utf-8"))
                else:
                    print("de connect!")
                    return
            elif fd == sys.stdin.fileno():
                try:
                    data = input()
                except EOFError:
                    print("I want to exit")
                    return
                new_client.send(data.encode("utf-8"))
    new_client.close()
    s.close()


if __name__ == '__main__':
    tcp_server()
