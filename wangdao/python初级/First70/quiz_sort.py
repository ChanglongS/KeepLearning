#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_sort.py
# Date      :2024.10.26
# Time      :15:38
# Author    :Sun Chang long
# Email     :1204403199@qq.com

# 65. Python 实现二分查找（列表元素自定）
def binary_sort(my_list, num):
    list_binary = sorted(my_list)
    # print(list_binary)
    list_length = len(list_binary) - 1
    head = 0
    while head <= list_length:
        mid = (head + list_length) // 2
        if list_binary[mid] == num:
            print(f"{num}存在")
            return
        elif list_binary[mid] < num:
            head = mid + 1
        elif list_binary[mid] > num:
            list_length = mid - 1
    print(f"{num} 不存在")


# 66. Python 线性查找（列表元素自定）
def search_line(my_list, num):
    list_line = sorted(my_list)
    # print(list_line)
    for item in list_line:
        if item == num:
            print(f"{num}存在")
            return
    print(f"{num} 不存在")


# 67. Python 插入排序（列表元素自定）
def insert_sort(my_list):
    insert_list = sorted(my_list, reverse=True)
    print(insert_list)
    for i in range(1, len(insert_list)):
        j = i
        while j > 0:
            if insert_list[j] < insert_list[j - 1]:
                insert_list[j], insert_list[j - 1] = insert_list[j - 1], insert_list[j]
            j -= 1
    print(insert_list)


# 68. Python 快速排序（列表元素自定）
def partition(quick_list, low, high):
    pivot = quick_list[low]
    i, j = low, high
    while i <= j:
        while i <= j and quick_list[i] <= pivot:
            i += 1
        while i <= j and quick_list[j] >= pivot:
            j -= 1
        if i <= j:
            quick_list[i], quick_list[j] = quick_list[j], quick_list[i]
    quick_list[low], quick_list[j] = quick_list[j], quick_list[low]
    return j


def quick_sort(quick_list, low, high):
    if low < high:
        pi = partition(quick_list, low, high)
        quick_sort(quick_list, low, pi - 1)
        quick_sort(quick_list, pi + 1, high)


# 69. Python 选择排序（列表元素自定）
def select_sort(my_list):
    arr = my_list.copy()
    print(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


# 70. Python 冒泡排序（列表元素自定）
def pop_sort(my_list):
    arr = my_list.copy()
    print(arr)
    for i in range(len(arr)):
        flag = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    print(arr)


# 74. Python 希尔排序（列表元素自定）
def shell_sort(my_list):
    arr = my_list.copy()
    print(arr)
    div = len(arr) // 2
    while div > 0:
        for i in range(div, len(arr)):
            j = i
            while j >= div:
                if arr[j] < arr[j - div]:
                    arr[j], arr[j - div] = arr[j - div], arr[j]
                j -= div
        div //= 2
    print(arr)


# 72. Python 堆排序(列表元素自定)
def heapify(heap_list, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and heap_list[left] > heap_list[largest]:
        largest = left
    if right < n and heap_list[right] > heap_list[largest]:
        largest = right
    if largest != i:
        heap_list[i], heap_list[largest] = heap_list[largest], heap_list[i]
        heapify(heap_list, n, largest)


def heap_sort(my_list):
    heap_list = my_list.copy()
    n = len(heap_list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap_list, n, i)
    for i in range(n - 1, 0, -1):
        heap_list[i], heap_list[0] = heap_list[0], heap_list[i]
        heapify(heap_list, i, 0)
    print(heap_list)


# 71. Python 归并排序(列表元素自定)
def merge(left, right) -> list:
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


def merge_sort(merge_list) -> list:
    # print(merge_list)
    if len(merge_list) <= 1:
        return merge_list
    mid = len(merge_list) // 2
    left = merge_sort(merge_list[:mid])
    right = merge_sort(merge_list[mid:])

    return merge(left, right)


# 73. Python 计数排序(列表元素自定)


if __name__ == "__main__":
    run_code = 0
    my_list = [10, 3, 4, 9, 2, 11, 5, 1, 8, 0, 6]
    print(my_list)
    print("-" * 50)

    binary_sort(my_list, 7)
    print("-" * 50)

    search_line(my_list, 7)
    print("-" * 50)

    insert_sort(my_list)
    print("-" * 50)

    quick_list = my_list.copy()
    print(quick_list)
    quick_sort(quick_list, 0, len(quick_list) - 1)
    print(quick_list)
    print("-" * 50)

    select_sort(my_list)
    print("-" * 50)

    pop_sort(my_list)
    print("-" * 50)

    shell_sort(my_list)
    print("-" * 50)

    heap_sort(my_list)
    print("-" * 50)

    merge_list = my_list.copy()
    print("merge_sort result is : ", end="")
    print(merge_sort(merge_list))
    print("-" * 50)
