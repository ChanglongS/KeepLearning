#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_10.py
# Time      : 16:17
# Author    :SunChanglong


def printHeart():
    for i in range(4):
        for j in range(3 - i):
            print(" ", end="")
        for j in range(i + 2):
            print("* ", end="")
        for j in range(6 - i * 2):
            print(" ", end="")
        for j in range(i + 2):
            print("* ", end="")
        print()

    for i in range(10):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(9 - i):
            print("* ", end="")
        print()
    pass


if __name__ == "__main__":
    run_code = 0
    printHeart()
