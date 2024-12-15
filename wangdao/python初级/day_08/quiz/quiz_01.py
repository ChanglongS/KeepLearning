#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_01.py
# Time      : 10:09
# Author    :SunChanglong

def sum2(*args, **kwargs):
    print(args)
    print(kwargs)


def sum(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    print(*args)
    sum2(*args, **kwargs)


if __name__ == "__main__":
    run_code = 0
    sum(1, 2, 3, 4, 5, name="chang", age=18)
