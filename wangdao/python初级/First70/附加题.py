#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :附加题.py
# Date      :2024.10.26
# Time      :15:00
# Author    :Sun Chang long
# Email     :1204403199@qq.com


# 51. Python 判断字符串是否存在子字符串 （字符串内容自定）
def is_str():
    str51 = "abcdefghijklmn"
    str51_2 = "ijk"
    print(str51.find(str51_2))
    if str51.find(str51_2) != -1:
        return True
    return False


# 52. Python 判断字符串长度 （字符串内容读取输入获得）
def is_len():
    str52 = "abcdefg hijkl %mn"
    print(len(str52))


# 53. Python 使用正则表达式提取字符串中的 URL（字符串内容自定）
# 54. Python 将字符串作为代码执行（字符串内容自定）

# 55. Python 字符串翻转（字符串内容自定）
def is_reverse():
    str55 = "hi,i am fine, thank you, and you?"
    print(str55[::-1])


# 56. Python 对字符串切片及翻转（字符串内容自定）
def reverse_part():
    str56 = "hi,i am fine, thank you, and you?"
    new_str = str56[:1:] + str56[1:6][::-1] + str56[6:]
    print(new_str)


# 57. Python 按键(key)或值(value)对字典进行排序（字典内容自定）
def dict_sort():
    dict57 = {"sun": 1, "chang": 2, "long": 3}
    sort_value = sorted(dict57.items(), key=lambda x: x[0])
    print(sort_value)
    sort_value = sorted(dict57.items(), key=lambda x: x[1])
    print(sort_value)


# 58. Python 计算字典值之和（字典内容自定）
def dict_value_sum():
    dict58 = {"sun": 1, "chang": 2, "long": 3}
    print(list(dict58.keys()))
    sum = 0
    for item in dict58.values():
        sum += item
    print(sum)


# 59. Python 移除字典A和字典B中共同存在的键值对，各自独有的不移除（字典内容自定）
def del_same_key():
    dict59 = {"sun": 1, "chang": 2, "long": 3}
    dict59_2 = {"sun": 1, "chang": 2, "ning": 3}
    print(dict59.get("ning"))
    list_key_59 = list(dict59.keys())
    list_key_59_2 = list(dict59_2.keys())
    print(list_key_59)
    print(list_key_59_2)
    for key in list_key_59:
        if not dict59_2.get(key):
            continue
        else:
            dict59.pop(key)
            dict59_2.pop(key)
    print(dict59)
    print(dict59_2)


# 60. Python 合并字典A和字典B（字典内容自定）
def union_dict():
    dict60 = {"sun": 1, "chang": 2, "long": 3}
    dict60_2 = {"sun": 1, "chang": 2, "ning": 3}
    dict60.update(dict60_2)
    print(dict60)


# 61. 读取某个字符串时间，将字符串的时间转换为时间戳（时间戳是以秒数来表示当前时间的
# 一种时间形式）
def str_time():
    str61 = "15:33"
    list61 = str61.split(":")
    print(list61)
    sum_second = int(list61[0]) * 60 + int(list61[1])
    print(sum_second)


if __name__ == "__main__":
    run_code = 0
    is_str()
    print("-" * 50)
    is_len()
    print("-" * 50)
    is_reverse()
    print("-" * 50)
    reverse_part()
    print("-" * 50)
    dict_sort()
    print("-" * 50)
    dict_value_sum()
    print("-" * 50)
    del_same_key()
    print("-" * 50)
    union_dict()
    print("-" * 50)
    str_time()
    print("-" * 50)
    str_time()
    print("-" * 50)
