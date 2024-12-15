#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :excise.py
# Date      :2024.10.30
# Time      :21:05
# Author    :Sun Chang long
# Email     :1204403199@qq.com
import random
import time


class MySort(object):
    def __init__(self, length):
        self.arr = []
        self.length = length

    def init_list(self):
        for i in range(self.length):
            self.arr.append(random.randint(0, 99))

    def print_list(self, sort_method, *args, **kwargs):
        start = time.time()
        print(self.arr)
        if sort_method == self.merge_sort:
            self.arr = self.merge_sort(*args, **kwargs)
        sort_method(*args, **kwargs)
        print(self.arr)
        end = time.time()
        print(end - start)

    def adjust_heap(self, father, n):
        left = 2 * father + 1
        right = 2 * father + 2
        i = father
        if left < n and self.arr[left] > self.arr[father]:
            father = left
        if right < n and self.arr[right] > self.arr[father]:
            father = right
        if father != i:
            self.arr[i], self.arr[father] = self.arr[father], self.arr[i]
            self.adjust_heap(father, n)

    def heap_sort(self, father, n):
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.adjust_heap(i, n)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.adjust_heap(0, i)
        pass

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, arr2):
        if len(arr2) <= 1:
            return arr2
        mid = len(arr2) // 2
        left = self.merge_sort(arr2[:mid])
        right = self.merge_sort(arr2[mid:])
        return self.merge(left, right)

    def count_sort(self):
        count = [0] * 100
        for i in range(self.length):
            count[self.arr[i]] += 1
        k = 0
        for i in range(100):
            j = 0
            while j < count[i]:
                self.arr[k] = i
                j += 1
                k += 1


if __name__ == "__main__":
    run_code = 0
    my_list = MySort(10)
    my_list.init_list()
    # my_list.print_list(my_list.heap_sort, 0, len(my_list.arr))
    # my_list.print_list(my_list.merge_sort, my_list.arr)
    my_list.print_list(my_list.count_sort)
