import pygame

from plane import *

#开始
pygame.init()

#display(窗口)
#set_mode()方法  刷新我们的屏幕
screen = pygame.display.set_mode((480,700))

#image.load
#步骤 1 加载图片数据
#步骤 2 绘制图片数据
#步骤 3 更新显示
#步骤一 加载图片数据
#自己的飞机
bg = pygame.image.load('/mnt/images/background.png')
screen.blit(bg,(0,0))
fly = pygame.image.load('/mnt/images/me1.png')

#设置英雄的位置
sjl = pygame.Rect(240,570,102,106)
screen.blit(fly,sjl)

#创建敌人飞机
a = GameSprite('/mnt/images/enemy2.png')
a.rect.x = 50
a.rect.y = 50
#精灵组
enemy_Group = pygame.sprite.Group(a)
#update 和 draw方法
enemy_Group.update()
enemy_Group.draw(screen)
pygame.display.update()
#游戏时钟
clolk = pygame.time.Clock()
while True:
    #设置频率
    clolk.tick(60)
    #捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
    if sjl.y == 0:
        sjl.y = 600
    else:
        #设置y轴的值
        sjl.y = sjl.y -1
    #重新设置一下背景
    screen.blit(bg,(0,0))
    
    #绘制英雄的坐标
    screen.blit(fly,sjl)
    #update 和 draw方法
    enemy_Group.update()
    enemy_Group.draw(screen)
    #更新屏幕
    pygame.display.update()

    pass 

#结束
pygame.quit()
