#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_62.py
# Date      :2024.10.26
# Time      :15:38
# Author    :Sun Chang long
# Email     :1204403199@qq.com
# 62. 输入一个日期，输出3天前的日期的年月日

list_monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_run_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        list_monthday[2] += 1


def which_day(year, month, day, num):
    is_run_year(year)
    while num:
        day -= 1
        if day == 0:
            month -= 1
            if month == 0:
                year -= 1
                month = 12
            day = list_monthday[month]
        num -= 1
    print(year, month, day)


# print(list_monthday)


if __name__ == "__main__":
    run_code = 0
    which_day(2000, 1, 1, 3)
