#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :RedBlackTree.py
# Date      :2024.11.01
# Time      :18:30
# Author    :Sun Chang long
# Email     :1204403199@qq.com


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = 0  # 0代表红色，1代表黑色
        self.parent = None


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def insert(self, node: RedBlackTreeNode):
        if self.root is None:
            self.root = node
        else:
            x = self.root
            while x:
                y = x
                if x.value > node.value:
                    x = x.left
                else:
                    x = x.right
            if y.value > node.value:
                y.left = node
            else:
                y.right = node
        self.color_rotate(node)

    def color_rotate(self, node):
        parent_name: RedBlackTreeNode = node.parent
        while parent_name and parent_name.color == 0:
            grandpa = parent_name.parent
            if parent_name == grandpa.left:
                uncle = grandpa.right
                # 情境三
                if uncle and uncle.color == 0:
                    parent_name.color = 1
                    grandpa.color = 0
                    uncle.color = 1
                    node = grandpa
                    parent_name = node.parent
                    continue
                # 情境四
                if node == parent_name.right:
                    left_rotate(parent_name, self)
                    parent_name, node = parent_name.left, node
                # 情境五
                right_rotate(parent_name.parent, self)
                parent_name.color = 1
                grandpa.color = 0
                break
            else:
                pass
            
        self.root.color = 1
        pass


def left_rotate(node, tree):
    if not node.right:
        # 判断一下node的右结点是否存在，如果不存在，则不需要旋转
        return
    node_right = node.right  # node_right保存node的右结点
    node_right.parent = node.parent  # 把node的右结点的父亲结点设置为node的父结点
    if node.parent is None:
        # 如果node结点父结点不存在，则把node结点的右结点node_right变成根结点
        tree.root = node_right
    elif node.parent.left == node:
        # 如果node结点是根结点的左孩子
        node.parent.left = node_right
    else:
        # node结点是根结点的右孩子
        node.parent.right = node_right
    if node_right.left:
        # 判断node_right结点是否有左结点，如果有左结点，需要把node_right的左孩子的parent设置为node
        node_right.left.parent = node
    node.right = node_right.left
    node_right.left = node
    node.parent = node_right


def right_rotate(node, tree):
    if not node.left:
        return
    node_left = node.left
    node_left.parent = node.parent
    if node.parent is None:
        tree.root = node_left
    elif node == node.parent.left:
        node.parent.left = node_left
    else:
        node.parent.right = node_left
    if node_left.right:
        node_left.right.parent = node
    node.left = node_left.right
    node_left.right = node
    node.parent = node_left


def main():
    my_list = [7, 1, 2, 4, 3, 6, 8]
    tree = RedBlackTree()
    for i in my_list:
        node = RedBlackTreeNode(i)
        tree.insert(node)
        del node


if __name__ == "__main__":
    run_code = 0
