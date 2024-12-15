#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :queue.py
# Date      :2024.10.29
# Time      :11:54
# Author    :Sun Chang long
# Email     :1204403199@qq.com

from collections import deque

MaxSize = 5


class Queue:
    def __init__(self):
        self.queue = []
        self.front = self.rear = 0

    def enqueue(self, value):
        if (self.rear + 1) % MaxSize == self.front:
            raise Exception("Queue is full")
        else:
            self.rear += 1
            self.queue.append(value)

    def dequeue(self):
        print(self.queue[self.front])
        self.front = (self.front + 1) % MaxSize


if __name__ == "__main__":
    run_code = 0
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.queue)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.front, end=' ')
    print(queue.rear)
