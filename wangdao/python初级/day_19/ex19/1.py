#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :1.py
# Date      :2024.11.09
# Time      :21:04
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 2、创建子进程，能够获取子进程pid并打印

from multiprocessing import Process
import os, time, random

def proc_pid():
    print(f"{os.getpid()}, father pid {os.getppid()}")


if __name__ == '__main__':
    p = Process(target=proc_pid)
    p.start()
