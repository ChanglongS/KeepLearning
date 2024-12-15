#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :4.py
# Date      :2024.11.09
# Time      :21:22
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 5、创建进程池，进程池中一个进程往queue中写，一个读并打印
from multiprocessing import Manager, Queue
from multiprocessing.pool import Pool
import random, os, time


def read(q: Queue):
    print(f"read pid {os.getpid()}")
    while not q.empty():
        print(q.get())


def write(q: Queue):
    print(f"write pid {os.getpid()}")
    for i in range(12):
        q.put_nowait(i)


if __name__ == '__main__':
    q = Manager().Queue()
    po = Pool(3)
    po.apply_async(write, (q,))
    po.apply_async(read, (q,))
    po.close()
    po.join()
