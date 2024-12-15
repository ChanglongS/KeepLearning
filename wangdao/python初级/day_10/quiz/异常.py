#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :异常.py
# Date      :2024.10.27
# Time      :18:16
# Author    :Sun Chang long
# Email     :1204403199@qq.com

def exception_classify():
    try:
        num = int(input("请输入一个数字: "))
        print(num)
    except ValueError:
        print("ValueError,请重新输入")
    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == "__main__":
    run_code = 0
    exception_classify()
