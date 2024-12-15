#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :进程池通信.py
# Date      :2024.11.09
# Time      :19:16
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from multiprocessing import Manager, Pool
import time, random, os


def read(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get())


def write(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "wangdao":
        q.put(i)


if __name__ == '__main__':
    q = Manager().Queue()
    po = Pool(3)
    po.apply_async(write, (q,))
    time.sleep(2)
    po.apply_async(read, (q,))
    po.close()
    po.join()
