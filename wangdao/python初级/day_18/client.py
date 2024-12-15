#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :client.py
# Date      :2024.11.08
# Time      :16:07
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
from socket import *
import struct
import os


class Client:
    def __init__(self, ip, port):
        self.client: socket = None
        self.path = os.getcwd()
        self.ip = ip
        self.port = port

    def tcp_connect(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.client.connect((self.ip, self.port))

    def send_train(self, data_bytes):
        train_head_bytes = struct.pack('I', len(data_bytes))
        self.client.send(train_head_bytes + data_bytes)

    def recv_train(self):
        train_head_bytes = self.client.recv(4)
        data_bytes_tuple = struct.unpack('I', train_head_bytes)
        return self.client.recv(data_bytes_tuple[0])

    def send_command(self):
        while True:
            command = input()
            self.send_train(command.encode('utf-8'))
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'cd':
                self.do_cd()
            elif command[:2] == 'rm':
                self.do_rm()
            elif command[:4] == 'gets':
                self.do_gets(command.split(' ')[1])
            elif command[:4] == 'puts':
                self.do_puts(command.split(' ')[1])
            else:
                print('wrong command')

    def do_puts(self, command):
        file_name = command
        f = open(file_name, 'rb')
        content = f.read()
        self.send_train(content)
        print(f"{file_name} is uploaded")

    def do_gets(self, command):
        file_name = command + '_stoc'
        # print(file_name)
        content = self.recv_train().decode('utf-8')
        print(content)
        f = open(file_name, "wb")
        f.write(content.encode('utf-8'))
        f.close()
        print(f"{file_name} is saved")

    def do_ls(self):
        data = self.recv_train().decode('utf-8')
        print(data)

    def do_pwd(self):
        data = self.recv_train().decode('utf-8')
        print(data)

    def do_cd(self):
        data = self.recv_train().decode('utf-8')
        print(data)

    def do_rm(self):
        data = self.recv_train().decode('utf-8')
        print(data)


if __name__ == '__main__':
    client = Client('192.168.212.105', 2000)
    # print(client.path)
    client.tcp_connect()
    client.send_command()
