#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :1.py
# Date      :2024.11.12
# Time      :21:42
# Author    :Sun Chang long
# Email     :changlong.sun0216@gmail.com


import re
import socket


def service_client(new_client):
    request = new_client.recv(1024).decode('utf-8')
    request_line = request.splitlines()
    print(request_line)
    if request_line:
        file_name = ''
        ret = re.match("[^/]+(/[^ ]*)", request_line[0])
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'

        try:
            f = open('./html' + file_name, 'rb')
        except:
            request = "HTTP/1.1 404 Not Found\r\n"
            request += "\r\n"
            request += "file not found"
            new_client.send(request.encode("utf-8"))
        else:
            request = "HTTP/1.1 200 OK\r\n"
            request += "\r\n"
            new_client.send(request.encode("utf-8") + f.read())
            f.close()
    new_client.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 20000))
    s.listen(100)

    while True:
        new_client, client_addr = s.accept()
        service_client(new_client)
    pass


if __name__ == '__main__':
    main()
