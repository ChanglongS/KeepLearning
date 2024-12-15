#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_05.py
# Time      : 10:56
# Author    :SunChanglong

class Animal:
    def eat(self):
        print("eat")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} bark")

    def eat(self):
        print("Dog eat")


class Cat(Animal):
    def eat(self):
        print("Cat eat")

    def bark(self):
        print("Cat bark")


class XiaoTianQuan(Dog):
    def bark(self):
        super().bark()
        print("XiaoTianQuan bark")

    def eat(self):
        print("XiaoTianQuan eat")


if __name__ == "__main__":
    run_code = 0
    dahuang = Dog("dahuang")
    dahuang.bark()
    dahuang.eat()

    tiandog = XiaoTianQuan("tiquan")
    tiandog.bark()
    tiandog.eat()
    print("-" * 50)
    print(dir(Animal))
    print('-' * 50)
    print(dir(Dog))
    print('-' * 50)
    print(dir(Cat))
    print('-' * 50)
