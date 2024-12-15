#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_02.py
# Time      : 10:18
# Author    :SunChanglong

def nam(name, age=18, gender=True):
    if gender:
        print(f"{name},age:{age},gender:male")
    else:
        print(f"{name},age:{age},gender:female")


if __name__ == "__main__":
    run_code = 0
    nam("long", 18)
    nam("mei", age=17, gender=False)
