#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :async.py
# Date      :2024.11.10
# Time      :20:54
# Author    :Sun Chang long
# Email     :changlong.sun@gmail.com


import asyncio


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(main())

