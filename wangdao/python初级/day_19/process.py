#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :process.py
# Date      :2024.11.09
# Time      :14:46
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
from multiprocessing import Process
import time
import os


def proc(name, age , **kwargs):
    for i in range(10):
        print(f"name = {name}, age = {age}, {kwargs}")
        print(f"proc {os.getpid()}, father pid is {os.getppid()}")
        time.sleep(0.2)


if __name__ == '__main__':
    p = Process(target=proc, args=('xiongda', 23), kwargs={'n408': 104})
    p.start()
    time.sleep(1)
    p.terminate()
    p.join()
    print(f"main {os.getpid()}, father pid is {os.getppid()}")

