#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :chat_server.py
# Date      :2024.11.07
# Time      :19:41
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

import sys
import socket
import select


def chat_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("", 2000)
    s.bind(addr)
    s.listen(5)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    client_list = []
    while True:
        events = epoll.poll(-1)
        for fp, event in events:
            if fp == s.fileno():
                new_client, client_addr = s.accept()
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client = None
                for client in client_list:
                    if fp == client.fileno():
                        data = client.recv(1024)
                        if data:
                            for other_client in client_list:
                                if other_client is client:
                                    pass
                                else:
                                    other_client.send(data)
                        else:
                            remove_client = client
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()
    s.close()
