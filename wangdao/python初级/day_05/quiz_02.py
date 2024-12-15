#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_02.py
# Time      : 15:56
# Author    :SunChanglong
# 2、打印九九乘法表


def printTable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} * {i} = {i * j}", end="\t")
        print()

if __name__ == "__main__":
    run_code = 0
    printTable()