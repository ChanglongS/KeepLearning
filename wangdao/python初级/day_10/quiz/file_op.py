#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :file_op.py
# Date      :2024.10.29
# Time      :09:47
# Author    :Sun Chang long
# Email     :1204403199@qq.com
import os


def file_op():
    file = open("file.txt", "w+", encoding="utf-8")
    file.write("人生苦短，我用python")
    file.close()


def file_readline():
    file = open("file.txt", "r", encoding="utf-8")
    # for item in file:
    #     print(item, end="")
    # print()
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
    file.close()


def file_readme():
    file = open("file.txt", "r", encoding="utf-8")
    file1 = open("file2.txt", "w", encoding="utf-8")
    text_file = file.read()
    file1.write(text_file)
    file1.close()
    file.close()


def file_seek():
    file = open("file.txt", "r", encoding="utf-8")
    file.seek(12, os.SEEK_SET)
    print(file.read())
    file.close()


def file_name():
    file = open("file.txt", "r", encoding="utf-8")
    os.rename("file2.txt", "file3.txt")
    file.close()


def file_delete():
    os.remove("file3.txt")


def package_add():
    os.mkdir("./package")
    file = open("./package/text.txt", "w", encoding="utf-8")
    file.write("BLG Fighting!!!")
    file.close()


def package_delete():
    os.rmdir("./package.txt")


def dfs_file(path, width):
    file_list = os.listdir(path)
    for item in file_list:
        print(" " * width, item)
        if os.path.isdir(path + "/" + item):
            dfs_file(path + "/" + item, width + 4)


if __name__ == "__main__":
    run_code = 0
    # file_op()
    # file_readline()
    # file_readme()
    # file_seek()
    # file_name()
    # file_delete()
    # package_add()
    # package_delete()
    dfs_file(".", 4)
