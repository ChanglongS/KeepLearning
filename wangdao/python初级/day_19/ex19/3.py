#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :3.py
# Date      :2024.11.09
# Time      :21:13
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 4、创建两个子进程，一个子进程写消息队列，一个读消息队列（依次写入A，B，C），
# 确保写的内容，读的进程，读取完毕并打印

from multiprocessing import Process, Queue
import os, random, time


def read(q: Queue):
    print(f"read pid {os.getpid()}")
    while not q.empty():
        print(q.get())


def write(q):
    print(f"write pid {os.getpid()}")
    for i in ["A", "B", "C", "D"]:
        q.put(i)


if __name__ == '__main__':
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    pw.start()
    time.sleep(2)
    pr.start()
    pr.join()
    pw.join()
