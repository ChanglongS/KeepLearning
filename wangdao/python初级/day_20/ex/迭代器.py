#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :迭代器.py
# Date      :2024.11.10
# Time      :18:26
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
from collections.abc import Iterable
from typing import Iterator


class Mylist(object):
    def __init__(self):
        self.arr = []

    def add(self, value):
        self.arr.append(value)

    def __iter__(self):
        my_iter = MyIterator(self.arr)
        return my_iter


class MyIterator(object):
    def __init__(self, arr):
        self.current = 0
        self.arr = arr

    def __next__(self):
        current = self.current
        self.current += 1
        if self.current <= len(self.arr):
            return self.arr[current]
        else:
            raise StopIteration
        # return self.arr[current]

    def __iter__(self):
        return self


if __name__ == '__main__':
    my_list = Mylist()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    print(isinstance(my_list, Iterable))
    print(isinstance(my_list, Iterator))
    # i = iter(my_list)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    for i in my_list:
        print(i)
