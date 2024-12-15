#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :2.py
# Date      :2024.11.12
# Time      :08:52
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com
# 3、创建一个子线程work1，传递列表a，然后work1中给列表a添加元素，
# 然后创建线程work2，查看列表是否发生改变

import asyncio, time, os


async def work1(nums: list):
    nums.append(44)
    print(nums)


async def work2(nums: list):
    print(f"work2 nums is {nums}")


async def main():
    task1 = asyncio.create_task(work1(nums))
    task2 = asyncio.create_task(work2(nums))
    print(f"----start---{time.strftime('%X')}")
    await task1
    await task2
    print(f"----end---{time.strftime('%X')}")


if __name__ == '__main__':
    nums = [11, 22, 33]
    asyncio.run(main())
