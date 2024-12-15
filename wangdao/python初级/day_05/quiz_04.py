#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_04.py
# Time      : 16:10
# Author    :SunChanglong
# 4、统计一个整数对应的二进制数的1的个数。
# 输入一个整数（可正可负，负数就按64位去遍历即可），
# 输出该整数的二进制包含1的个数


def sumOne():
    num = 127
    i = 1
    sum = 0
    while i & num != 0:
        sum += 1
        i <<= 1
    print(sum)

if __name__ == "__main__":
    run_code = 0
    sumOne()