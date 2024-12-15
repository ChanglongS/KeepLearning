#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_03.py
# Time      : 15:59
# Author    :SunChanglong

def printSan():
    for i in range(5):
        for j in range(4 - i):
            print(" ", end="")
        for j in range(i + 1):
            print("* ", end="")
        print()

    for i in range(4):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(4 - i):
            print("* ", end="")
        print()
    pass


def printSan2():
    for i in range(5):
        for j in range(4 - i):
            print(" ", end="")
        print("*", end="")
        for j in range(2 * i - 1):
            print(" ", end="")
        if i != 0:
            print("*", end="")
        print()
    for i in range(4):
        for j in range(i + 1):
            print(" ", end="")
        print("*", end="")
        for j in range(5 - 2 * i):
            print(" ", end="")
        if i != 3:
            print("*", end="")
        print()
    pass


if __name__ == "__main__":
    run_code = 0
    printSan()
    print()
    printSan2()
