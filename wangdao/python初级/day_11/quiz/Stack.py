#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :Stack.py
# Date      :2024.10.29
# Time      :11:46
# Author    :Sun Chang long
# Email     :1204403199@qq.com

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop(-1)

    def length(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False


if __name__ == "__main__":
    run_code = 0
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    print(stack.length())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.stack)
