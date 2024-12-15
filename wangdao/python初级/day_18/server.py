#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :server.py
# Date      :2024.11.08
# Time      :16:06
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
import os
from socket import *
import struct


class Server:
    def __init__(self, ip, port):
        self.tcp_server: socket = None
        self.ip = ip
        self.port = port

    def tcp_init(self):
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_server.bind((self.ip, self.port))
        self.tcp_server.listen(100)
        self.tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def tcp_accept(self):
        new_client, client_addr = self.tcp_server.accept()
        user = User(new_client)
        user.deal_command()


class User:
    def __init__(self, new_client):
        self.new_client = new_client
        self.user_name = None
        self.path = os.getcwd()

    def send_train(self, data_bytes):
        train_head_bytes = struct.pack('I', len(data_bytes))
        self.new_client.send(train_head_bytes + data_bytes)

    def recv_train(self):
        train_head_bytes = self.new_client.recv(4)
        data_bytes_tuple = struct.unpack('I', train_head_bytes)
        return self.new_client.recv(data_bytes_tuple[0])

    def deal_command(self):
        while True:
            command = self.recv_train().decode("utf-8")
            print(command)
            if command[:2] == "ls":
                self.do_ls()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'cd':
                self.do_cd(command.split(" ")[1])
            elif command[:2] == 'rm':
                self.do_rm(command.split(' ')[1])
            elif command[:4] == 'gets':
                self.do_gets(command.split(' ')[1])
            elif command[:4] == 'puts':
                self.do_puts(command.split(' ')[1])
            else:
                print('wrong command')

    def do_ls(self):
        # 通过os.getcwd()获取此目录下的文件名列表
        dir_list = os.listdir(self.path)
        # 把所有文件的 文件名 + 文件的大小 放入字符串
        data = ''
        for string in dir_list:
            data += string + '\t\t' + str(os.stat(string).st_size) + '\n'
        # 把ls打印出的字符串发给client
        self.send_train(data.encode('utf-8'))

    def do_pwd(self):
        self.send_train(self.path.encode('utf-8'))

    def do_cd(self, command):
        # print(command)
        path = command
        os.chdir(path)
        self.path = os.getcwd()
        self.send_train(self.path.encode('utf-8'))

    def do_rm(self, command):
        file_name = command
        os.remove(file_name)
        self.do_ls()

    def do_gets(self, command):
        # 下载file文件
        file_name = command
        # print(self.do_pwd())
        f = open(file_name, 'rb')
        content = f.read()
        f.close()
        print(content)
        self.send_train(content)

    def do_puts(self, command):
        file_name = command + '_ctos'
        data = self.recv_train()
        f = open(file_name, "wb")
        f.write(data)
        f.close()


if __name__ == '__main__':
    server = Server('192.168.212.105', 2000)
    server.tcp_init()
    server.tcp_accept()
