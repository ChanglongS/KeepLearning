#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :异常传递.py
# Date      :2024.10.27
# Time      :18:29
# Author    :Sun Chang long
# Email     :1204403199@qq.com
def funC():
    raise Exception("Value is Error")


def funB():
    print("start funB")
    funC()
    print("end funB")


def funA():
    print("start funA")
    funB()
    print("end funA")


if __name__ == "__main__":
    run_code = 0
    try:
        funA()
    except Exception as e:
        print(e)
