#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_11.py
# Time      : 11:43
# Author    :SunChanglong
# 11. Python 读取字符串，判断是否为数字，是数字，输出 正确，否则输出 错误
# 12. Python 判断奇数偶数，读取输入，判断是奇数输出奇数，偶数，就输出偶数
# 13. Python 判断闰年，读取输入，判断如果是闰年，输出闰年，不是，输出平年
def strNum(str_num):
    print(str1.isdigit())
    print("-" * 50)
    num = int(input("输入一个数:"))
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
    print("-" * 50)
    year = int(input("输入一个年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("闰年")
    else:
        print("平年")
    print("-" * 50)


if __name__ == "__main__":
    run_code = 0
    str1 = "12832"
    strNum(str1)
