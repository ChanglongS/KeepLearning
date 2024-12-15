#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_01.py
# Time      : 15:55
# Author    :SunChanglong
# 1、实现从1到100之间的奇数求和


def sumOdd():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    run_code = 0
    print(sumOdd())
