# author luke
# 2022年02月24日


import wd_message
import pygame
def use_package():
    wd_message.send_message.send()

    txt = wd_message.recv_message.receive()
    print(txt)

if __name__ == '__main__':
    use_package()
