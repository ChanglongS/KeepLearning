#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :sort.py
# Date      :2024.10.29
# Time      :18:32
# Author    :Sun Chang long
# Email     :1204403199@qq.com
import random


class MySort(object):
    def __init__(self, list_len):
        self.arr = []
        self.list_len = list_len

    def init_list(self):
        for i in range(self.list_len):
            self.arr.append(random.randint(0, 99))

    def print_list(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
        print(self.arr)

    def pao_sort(self):
        for i in range(self.list_len - 1):
            for j in range(0, self.list_len - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def select_sort(self):
        for i in range(self.list_len):
            flag = i
            for j in range(i + 1, self.list_len):
                if self.arr[flag] > self.arr[j]:
                    flag = j
            self.arr[i], self.arr[flag] = self.arr[flag], self.arr[i]

    def insert_sort(self):
        for i in range(1, self.list_len):
            j = i
            while j > 0:
                if self.arr[j] < self.arr[j - 1]:
                    self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                j -= 1

    def partition(self, low, high):
        i, j = low, high
        pivot = self.arr[low]
        while i <= j:
            while i <= j and self.arr[i] <= pivot:
                i += 1
            while i <= j and self.arr[j] >= pivot:
                j -= 1
            if i <= j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[j], self.arr[low] = self.arr[low], self.arr[j]
        return j

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)


if __name__ == "__main__":
    run_code = 0
    sort_class = MySort(10)
    sort_class.init_list()
    # sort_class.print_list(sort_class.pao_sort)
    # sort_class.print_list(sort_class.select_sort)
    # sort_class.print_list(sort_class.insert_sort)
    sort_class.print_list(sort_class.quick_sort, 0, 9)
