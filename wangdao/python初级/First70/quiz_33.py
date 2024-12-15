#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_33.py
# Time      : 20:51
# Author    :SunChanglong
# 33. 写一个python list 的增删查改，list初始化几个元素自定
def listOp():
    list33 = [1, 2, "3"]
    list33.append("4")
    print(list33)
    list33.remove("3")
    print(list33)
    list33[2] = "2"
    print(list33)
    print(list33.index("2"))


# 34. 写一个python dict的增删查改，dict初始化几个键值对自定
def dictOp():
    dict34 = {"chang": 1, "long": 2, "sun": 3}
    dict34["yu"] = 4
    print(dict34)
    dict34.pop("chang")
    print(dict34)
    dict34["yu"] = 5
    print(dict34)
    print(dict34.get("sun"))


# 36. 计算列表中10个元素的立方和（10个元素值自定）
def listCheng():
    list36 = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    sumSan = 0
    for i in list36:
        sumSan += (i ** 3)
    print(sumSan)
    list36[1:9] = list36[1:9:][::-1]
    print(list36)


# 39. Python 将列表中的头尾两个元素对调（list内的元素自定）
def transHeadTail():
    list36 = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    num = len(list36)
    list36[0], list36[num - 1] = list36[num - 1], list36[0]
    print(list36)
    print(min(list36))
    print(max(list36))


# 50. Python 移除字符串中的指定位置字符（字符串内容自定，指定位置通过读取输入获取）
def removeStr():
    str1 = "abc dbc los ooifs"
    str2 = str1[:3:] + str1[4::]
    print(str2)


if __name__ == "__main__":
    run_code = 0
    listOp()
    print("-" * 50)
    dictOp()
    print("-" * 50)
    listCheng()
    print("-" * 50)
    transHeadTail()
    print("-" * 50)
    removeStr()
    print("-" * 50)
