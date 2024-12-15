#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :4.py
# Date      :2024.11.12
# Time      :09:23
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 7、自制迭代器并使用next及for in的处理
from typing import Iterable, Iterator


class Mylist(object):
    def __init__(self, arr):
        self.arr = arr

    def __iter__(self):
        my_iter = MyIterator(self.arr)
        return my_iter


class MyIterator(object):
    def __init__(self, arr):
        self.arr = arr
        self.index = 0

    def __next__(self):
        index = self.index
        self.index += 1
        if index < len(self.arr):
            return self.arr[index]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    nums = [11, 22, 33, 44, 55, 66, 77, 89]
    mylist = Mylist(nums)
    print(isinstance(mylist, Iterable))
    print(isinstance(mylist, Iterator))
    for i in mylist:
        print(i, end=" ")
    print()
