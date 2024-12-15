#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :2.py
# Date      :2024.11.14
# Time      :09:24
# Author    :Sun Chang long
# Email     :changlong.sun0216@gmail.com

import socket
import re
from multiprocessing import Process


def service_client(new_client):
    request = new_client.recv(1024).decode('utf-8')
    request_line = request.splitlines()[0]
    print(request_line)
    if request_line:
        ret = re.match('[^/]+([/ ]*)', request_line)
        file_name = ""
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
            try:
                f = open(file_name, "rb")
            except:
                request = "HTTP/1.1 404 Not Found\r\n"
                request += "\r\n"
                request += "Not Such File"
                new_client.send(request.encode("utf-8"))
            else:
                request = "HTTP/1.1 200 OK\r\n"
                request += "\r\n"
                content = f.read()
                new_client.send(request.encode("utf-8") + content)

    new_client.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 2000))
    s.listen(100)
    while True:
        new_client, client_addr = s.accept()
        p = Process(target=service_client, args=(new_client,))
        p.start()
        new_client.close()


if __name__ == '__main__':
    main()
