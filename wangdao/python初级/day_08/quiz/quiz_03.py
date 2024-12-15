#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_03.py
# Time      : 10:22
# Author    :SunChanglong
# 设计一个类，实例化两个对象，然后小明跑步跑完步，会去吃东西
# ，小美不跑步，小美喜欢吃东西
#
# •小明 今年 18 岁，身高 1.75，每天早上 跑 完步，会去 吃 东西
# •小美 今年 17 岁，身高 1.65，小美不跑步，小美喜欢 吃 东西

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name}今年{self.age}岁,身高{self.height},"

    def run(self):
        print(f"{self.name}跑完步,", end="")
        pass

    def eat(self):
        print(f"{self.name}喜欢吃东西.")
        pass


if __name__ == "__main__":
    run_code = 0
    xiaoming = Person("xiaoming", 18, 1.75)
    xiaomei = Person("xiaomei", 17, 1.65)
    print(xiaoming, end="")
    xiaoming.run()
    xiaoming.eat()
    print(xiaomei, end="")
    xiaoming.eat()
