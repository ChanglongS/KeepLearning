#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :进程池.py
# Date      :2024.11.09
# Time      :19:30
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from multiprocessing.pool import Pool
import time, os, random


def worker(msg):
    t_start = time.time()
    print(f"{msg}: {os.getpid()}, father pid = {os.getppid()}")
    time.sleep(random.random() * 2)
    t_end = time.time()
    print(t_end - t_start)


if __name__ == '__main__':
    po = Pool(3)
    for i in range(10):
        po.apply_async(worker, (i,))
    po.close()
    po.join()
