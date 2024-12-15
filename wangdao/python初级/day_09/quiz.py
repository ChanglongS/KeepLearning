#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz.py
# Date      :2024.10.26
# Time      :14:54
# Author    :SunChanglong
# Email     :1204403199@qq.com
# 类属性和类方法

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == "__main__":
    run_code = 0
    xiaoming = Person("xiaoming")
    print(Person.count)
    print(Person.get_count())
