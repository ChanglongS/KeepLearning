#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :单例.py
# Date      :2024.10.27
# Time      :18:16
# Author    :Sun Chang long
# Email     :1204403199@qq.com


class MusicOb(object):
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            print("创建空间")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, music_name):
        self.music_name = music_name


if __name__ == "__main__":
    run_code = 0
    player1 = MusicOb("zhoujielun")
    print(player1.music_name)
    player2 = MusicOb("linjunjie")
    print(player2.music_name)
    print(player1)
    print(player2)
