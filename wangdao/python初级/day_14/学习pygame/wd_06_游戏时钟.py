# 作者: 王道 龙哥
# 2022年03月01日15时17分44秒

import pygame

pygame.init()
# 3. 创建游戏时钟对象
clock = pygame.time.Clock()
i = 0

# 游戏循环
while True:

    # 设置屏幕刷新帧率，每秒60次
    clock.tick(1)

    print(i)
    i += 1

pygame.quit()