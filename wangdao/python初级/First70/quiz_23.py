#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_23.py
# Time      : 20:21
# Author    :SunChanglong

def maxDevide(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 % num2 != 0:
        maxDevide(num2, num1 % num2)
    else:
        print(num2)


# 24. 读取两个数，输出其最小公倍数算
def minCheck(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1 <<= 1
    print(num1)
    pass


# 25. 读取a+b，或者a-b，或者a*b，或者a/b这样的格式，实现简单的计算器功能，a和b输入时
# 是具体的数字
def calTect():
    str1 = input("str1:")
    num = 0
    if str1.count("+") != 0:
        num = float(str1.split("+")[0]) + float(str1.split("+")[1])
        pass
    elif str1.count("-") != 0:
        num = float(str1.split("-")[0]) - float(str1.split("-")[1])
        pass
    elif str1.count("*") != 0:
        num = float(str1.split("*")[0]) * float(str1.split("*")[1])
        pass
    elif str1.count("/") != 0:
        num = float(str1.split("/")[0]) / float(str1.split("/")[1])
        pass
    print(num)


# 27. 读取一个数，输出从1到该数字之间斐波那契数列，要求使用递归实现
def recursiveFib(num):
    list27 = [0, 1, 2]
    if num == 1:
        return 1
    if num == 2:
        return 2
    else:
        return recursiveFib(num - 1) + recursiveFib(num - 2)


# 29. Python读取两个字符串，判断是否相等，相等就输出 相等，不等输出不等
def sumStr(str1, str2):
    if str1 == str2:
        print("相等")
    else:
        print("不等")

    if str1.islower():
        str1 = str1.upper()
        print(str1)
    if str1.lower() == str2:
        print(str1)
    else:
        print(str1.lower())


if __name__ == "__main__":
    run_code = 0
    maxDevide(8, 12)
    minCheck(8, 12)
    calTect()
    num = int(input("num:"))
    for i in range(1, num + 1):
        print(recursiveFib(i), end=" ")
    print()
    sumStr("abcd", "abcd")
