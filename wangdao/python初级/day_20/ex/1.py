#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :1.py
# Date      :2024.11.12
# Time      :08:39
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com


# 1、创建多线程，查看saySorry打印效果（和上课一致即可）
import asyncio
import os
import time


async def say_sorry():
    print("sorry")


async def main():
    task = asyncio.create_task(say_sorry())
    print(f"===start---{time.strftime('%X')}")
    await task
    await asyncio.sleep(1)
    print(f"===end---{time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
