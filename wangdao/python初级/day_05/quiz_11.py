#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_11.py
# Time      : 08:54
# Author    :SunChanglong

def difTwoNum():
    my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
    num = 0
    for i in my_list:
        num ^= i
    mark = 1
    while (mark & num) == 0:
        mark <<= 1
    difOne = 0
    difTwo = 0
    for i in my_list:
        if (i & mark) == 0:
            difOne ^= i
        elif (i & mark) == 1:
            difTwo ^= i
    print(difOne, difTwo)


if __name__ == "__main__":
    run_code = 0
    difTwoNum()
