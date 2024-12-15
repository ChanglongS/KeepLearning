#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :Thread.py
# Date      :2024.11.10
# Time      :15:15
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from threading import Thread, Lock
import time

num = 1000000


def thread1(nums: list, mutex: Lock):
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
    print(f"thread1 num is : {num}")


def thread2(nums, mutex2: Lock):
    global num
    for i in range(1000000):
        mutex2.acquire()
        num += 1
        mutex2.release()
    print(f"thread2 num is : {num}")


def test():
    nums = [11, 22, 33]
    # num = 1000
    mutex = Lock()
    mutex2 = Lock()
    t1 = Thread(target=thread1, args=(nums, mutex))
    t2 = Thread(target=thread2, args=(nums, mutex2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)


if __name__ == '__main__':
    test()
