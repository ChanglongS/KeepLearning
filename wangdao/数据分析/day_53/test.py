#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :test.py
# Date      :2024.11.27
# Time      :09:13
# Author    :Sun Chang long
# Email     :changlong.sun0216@gmail.com
def decreasing_first_fit(items, C):
    # 将物品按体积从大到小排序
    items.sort(reverse=True)

    bins = []  # 存储箱子的列表
    for item in items:
        placed = False
        # 尝试将物品放入现有的箱子中
        for bin in bins:
            if sum(bin) + item <= C:
                bin.append(item)
                placed = True
                break
        # 如果当前所有箱子都无法容纳该物品，则开启一个新的箱子
        if not placed:
            bins.append([item])

    # 返回箱子的总数和每个箱子的内容
    return len(bins), bins


# 测试案例1
items1 = [5, 7, 3, 8, 4, 2]
C1 = 10
num_bins1, bins1 = decreasing_first_fit(items1, C1)
print("Test Case 1:")
print(f"Number of bins: {num_bins1}")
print(f"Bins: {bins1}")

# 测试案例2
items2 = [6, 2, 4, 8, 7, 5, 3]
C2 = 10
num_bins2, bins2 = decreasing_first_fit(items2, C2)
print("\nTest Case 2:")
print(f"Number of bins: {num_bins2}")
print(f"Bins: {bins2}")
