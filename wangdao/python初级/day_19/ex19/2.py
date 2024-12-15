#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :2.py
# Date      :2024.11.09
# Time      :21:08
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

# 3、给子进程传参，查看子进程修改了传递的列表中的值以后，父进程中是否会变化，
# 子进程修改全局变量，父进程join子进程后，打印全局变量是否变化

from multiprocessing import Process
import os, time, random

nums = [11, 22, 33]


def add1():
    print("add1 :", end=" ")
    nums.append(44)
    print(nums)


def add2():
    print(nums)
    print("add2 :", end=" ")
    nums.append(55)
    print(nums)


if __name__ == '__main__':
    padd1 = Process(target=add1)
    padd2 = Process(target=add2)
    padd1.start()
    time.sleep(1)
    padd2.start()
    padd1.join()
    padd2.join()
    print(f"father is {nums}")
