#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :async2.py
# Date      :2024.11.10
# Time      :20:59
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com


import asyncio
import time


async def print_num(delay, name):
    await asyncio.sleep(delay)
    print(name)


# async def main():
#   •	await asyncio.create_task(print_num(1, '1'))：
# 	•	立即创建并等待任务 print_num(1, '1')，执行时间为 1 秒。
# 	•	await asyncio.create_task(print_num(2, '2'))：
# 	•	等待第一个任务完成后，再创建并等待第二个任务 print_num(2, '2')，执行时间为 2 秒。
# 	•	因为两个任务是顺序执行的，先执行 1 秒任务，再执行 2 秒任务，所以总时间为 1 + 2 = 3 秒。
#     print(f"----start----{time.strftime('%X')}")
#     await asyncio.create_task(print_num(1, '1'))
#     await asyncio.create_task(print_num(2, '2'))
#     print(f"----end----{time.strftime('%X')}")

async def main():
    # 	•	task1 = asyncio.create_task(print_num(1, '1')) 和 task2 = asyncio.create_task(print_num(2, '2'))：
    # 	•	两个任务同时创建。
    # 	•	await task1 和 await task2：
    # 	•	任务 并发执行，而不是顺序执行。
    # 	•	print_num(1, '1') 和 print_num(2, '2') 同时运行，任务会一起完成。
    # 	•	总时间是 max(1, 2) = 2 秒，因为两个任务的执行时间互不影响。
    task1 = asyncio.create_task(print_num(1, '1'))
    task2 = asyncio.create_task(print_num(2, '2'))
    print(f"----start---- {time.strftime('%X')}")
    await task1
    await task2
    print(f"----end---- {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
