#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_05.py
# Time      : 16:12
# Author    :SunChanglong
# 5、有101个整数，其中有50个数出现了两次，
# 1个数出现了一次， 找出出现了一次的那个数。
# （大家使用7个数即可）

def difOne():
    my_list = [1, 1, 2, 2, 3, 3, 4]
    num = 0
    for i in my_list:
        num ^= i
    print(num)


if __name__ == "__main__":
    run_code = 0
    difOne()
