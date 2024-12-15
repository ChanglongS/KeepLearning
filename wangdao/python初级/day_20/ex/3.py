#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :3.py
# Date      :2024.11.12
# Time      :09:00
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 4、创建两个子线程，分别对同一个全局变量加1百万，查看最终结果是否为2百万，
# 如果不为2百万，通过加解锁后，实现最终是2百万（电脑速度过快的同学，可以搞2千万）
# 5、制造死锁问题，并用ps查看线程状态

import threading
import time, os


def work1(nums):
    global g_nums
    for i in range(nums):
        mutex1.acquire()
        g_nums += 1
        mutex1.release()
    print(f"work1 nums is {g_nums}")


def work2(nums):
    global g_nums
    for i in range(nums):
        mutex2.acquire()
        g_nums += 1
        mutex2.release()
    print(f"work2 nums is {g_nums}")


if __name__ == '__main__':
    nums = 10000000
    g_nums = 10000000
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    t1 = threading.Thread(target=work1, args=(nums,))
    t2 = threading.Thread(target=work2, args=(nums,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"nums is {g_nums}")
