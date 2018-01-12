
import pygame
from plane_sprites2 import *


class PlaneGame(object):
    '''飞机大战主游戏类'''
    def __init__(self):
        '''初始化游戏'''
        #1 窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #背景  英雄  敌机  这些精灵
        self.__create_sprites()
    def start_game(self):
        '''开始游戏'''                       
        print('y游戏开始')
        while True:
            #设置帧率
            self.clock.tick(60)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新精灵组
            self.__update_sprites()
            #更新屏幕显示
            pygame.display.update()
    def __event_handler(self):
        '''监听事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#退出
                pygame.__game_over()  
    @staticmethod
    def __game_over(): 
        pygame.quit()
        exit()
    def __check_collide(self):
        '''碰撞检测'''
        pass
    def __update_sprites(self):
        '''更新精灵组'''
        pass
    def __create_sprites(self):
        '''创建精灵用'''
        pass
if __name__ == '__main__':
    #创建游戏对向'''
    game = PlaneGame()
    #开始游戏'''
    game.start_game()

