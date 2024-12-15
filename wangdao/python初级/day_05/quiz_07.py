#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_07.py
# Time      : 16:15
# Author    :SunChanglong
# 写一个say_hello函数打印多次hello并给该函数加备注
# （具体打印几次依靠传递的参数），然后调用say_hello，
# 同时学会快速查看函数备注快捷键，及如何跳转到函数实现快捷键
import quiz_model


def say_hello():
    print("Hello World!")


if __name__ == "__main__":
    run_code = 0
    say_hello()
    quiz_model.printTest()
