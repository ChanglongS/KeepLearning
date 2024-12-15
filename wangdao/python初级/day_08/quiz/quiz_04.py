#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_04.py
# Time      : 10:36
# Author    :SunChanglong
# •一只 黄颜色 的 狗狗 叫 大黄
# •具有  汪汪叫 行为
# •具有  摇尾巴 行为

class Dog:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"一只{self.color}颜色的狗狗叫{self.name}"
        pass

    def __del__(self):
        print("飞起来")
        pass

    def crash(self):
        print("汪汪叫")

    def tail(self):
        print("摇尾巴")


if __name__ == "__main__":
    run_code = 0
    dahuang = Dog("yellow", "dahuang")
    print(dahuang)
    dahuang.crash()
    dahuang.tail()
