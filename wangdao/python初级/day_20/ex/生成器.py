#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :生成器.py
# Date      :2024.11.10
# Time      :18:40
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com

from collections.abc import Iterable


def fib(times):
    num = 0
    num1, num2 = 0, 1
    for it in range(times):
        num = num1
        num1, num2 = num2, num1 + num2
        yield num
    return num


if __name__ == '__main__':
    f = fib(10)
    print(isinstance(f, Iterable))
    for i in f:
        print(i, end=" ")
    print()