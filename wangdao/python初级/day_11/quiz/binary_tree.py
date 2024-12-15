#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :binary_tree.py
# Date      :2024.10.29
# Time      :12:23
# Author    :Sun Chang long
# Email     :1204403199@qq.com
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


class BinaryTree:
    # 层序建树
    def __init__(self):
        self.root = None
        self._queue = deque()

    def insert_node(self, value):
        node = Node(value)
        self._queue.append(node)
        if self.root is None:
            self.root = node
        else:
            if self._queue[0].lchild is None:
                self._queue[0].lchild = node
            elif self._queue[0].rchild is None:
                self._queue[0].rchild = node
                self._queue.popleft()

    def preOrder(self, cur_node: Node):
        if cur_node:
            print(cur_node.value, end=" ")
            self.preOrder(cur_node.lchild)
            self.preOrder(cur_node.rchild)


if __name__ == "__main__":
    run_code = 0
    list_node = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_tree = BinaryTree()
    for i in list_node:
        binary_tree.insert_node(i)
    binary_tree.preOrder(binary_tree.root)
