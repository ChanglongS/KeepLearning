#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :5.py
# Date      :2024.11.14
# Time      :11:13
# Author    :Sun Chang long
# Email     :changlong.sun0216@gmail.com
import select
import socket
import re


def server_client(new_client, data):
    request_line = data.splitlines()[0]
    if request_line:
        ret = re.match("[^/]+([^ ]*)", request_line)
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"

            try:
                f = open(file_name, "rb")
            except:
                request = "HTTP/1.1 404 Not Found\r\n"
                request += "\r\n"
                request += "no such file"
                new_client.send(request.encode("utf-8"))
            else:
                request = "HTTP/1.1 200 OK\r\n"
                request += "\r\n"
                content = f.read()
                new_client.send(request.encode("utf-8") + content)
                f.close()
    new_client.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8080))
    s.listen(100)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    client_dict = dict()
    while True:
        events = epoll.poll()
        for fd, event in events:
            if fd == s.fileno():
                new_client, client_addr = s.accept()
                client_dict[new_client.fileno] = new_client
                epoll.register(new_client.fileno(), select.EPOLLIN)
            elif event == select.EPOLLIN:
                data = client_dict[fd].recv(1024).decode("utf-8")
                if data:
                    server_client(client_dict[fd], data)
                else:
                    client_dict[fd].close()
                    client_dict.pop(fd)
                    epoll.unregister(client_dict[fd].fileno())


if __name__ == '__main__':
    main()
