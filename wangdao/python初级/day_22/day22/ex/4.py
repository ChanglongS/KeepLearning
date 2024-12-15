#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :4.py
# Date      :2024.11.14
# Time      :10:30
# Author    :Sun Chang long
# Email     :changlong.sun0216@gmail.com

import sys, socket
import re


class WSBFServer(object):
    def __init__(self, port, document_root):
        self.port = port
        self.document_root = document_root
        self.client_list = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('', self.port))
        self.s.listen(100)
        self.s.setblocking(False)

    def run_forever(self):
        while True:
            new_client, client_addr = self.s.accept()
            self.client_list.append(new_client)
            new_client.setblocking(False)
            for client in self.client_list:
                try:
                    request = client.recv(1024).decode("utf-8")
                except:
                    pass
                else:
                    if request:
                        self.deal_with_client(request, new_client)
                    else:
                        client.close()
                        self.client_list.remove(client)

    def deal_with_client(self, request, new_client):
        request_line = request.splitlines()[0]
        file_name = ""
        if request_line:
            ret = re.match("([^/]+)([^ ]*)", request_line)
            if ret:
                file_name = ret.group(2)
                if file_name == "/":
                    file_name = "/index.html"

            try:
                f = open(self.document_root + file_name, "rb")
            except:
                request_body = "not such file"
                request_head = "HTTP/1.1 404 Not Found\r\n\r\n"
                new_client.send(request_head.encode("utf-8") + request_body.encode("utf-8"))
            else:
                request_body = f.read()
                request_head = "HTTP/1.1 200 OK\r\n\r\n"
                new_client.send(request_head.encode("utf-8") + request_body)
            new_client.close()


DOCUMENT_ROOT = "./html"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    port = int(sys.argv[1])
    server = WSBFServer(port, DOCUMENT_ROOT)
    server.run_forever()
