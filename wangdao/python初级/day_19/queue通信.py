#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :queue通信.py
# Date      :2024.11.09
# Time      :19:15
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from multiprocessing import Process, Queue
import os
import time


def read(q):
    print(f"pid = {os.getpid()}, father pid = {os.getppid()}")
    while not q.empty():
        print(q.get())


def write(q):
    print(f"pid = {os.getpid()}, father pid = {os.getppid()}")
    for i in "wangdao":
        q.put(i, False)


if __name__ == '__main__':
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    pw.start()
    time.sleep(2)
    pr.start()
    pw.join()
    pr.join()
