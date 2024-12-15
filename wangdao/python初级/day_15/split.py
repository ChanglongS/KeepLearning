#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :split.py
# Date      :2024.11.02
# Time      :21:03
# Author    :Sun Chang long
# Email     :1204403199@qq.com



str2 = "对于具有奇数 内 核 大 小 和 步 长 为1的 稀 疏 卷 积, 对 应  于 核 偏 移 量(a, b, c)的 映 射 总 是 与 对 应 于 对 称 核  偏 移 量(−a, −b, −c)的 映 射 具 有 相 同 的 大 小。"
str3 = "".join([i for i in str2 if i != " "])
print(str3)
