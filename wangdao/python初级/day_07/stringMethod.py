#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :stringMethod.py
# Time      : 12:46
# Author    :SunChanglong


def string_method():
    num = "123"
    print(num.isdecimal())
    num_2 = "hello"
    print(num_2.isupper())  # 判断是否全是大写
    print(num_2.upper())
    num_3 = "ABC"
    print(num_3.islower())  # 判断是否全是小写
    print(num_3.lower())

    num_4 = "     hello   world   "
    print(num_4.strip())

    num_5 = "hello,world,hi,limeimei,love,you"
    print(num_5.split(","))
    num_6 = num_5.replace(",", " ")
    print(num_6)
    print(num_6.split(" "))

    str1 = "hello\nworld\nhi"
    print(str1.splitlines())

    str2 = "python"
    print(str2[-2:: ])
    print(str2[::-1])

    my_list = ["h","e","l","o","u"]
    print(str(my_list))
    print("".join(my_list))

    my_list2 = [1,2]
    my_list3 = [3,4]
    my_list2.extend(my_list3)
    print(my_list2)
    my_list2.append(my_list3)
    print(my_list2)

if __name__ == "__main__":
    string_method()
    run_code = 0
