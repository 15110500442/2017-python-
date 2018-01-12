import pygame
from plane_sprite import *
class PlaneGame(object):
    '''飞机大战主游戏'''    
    def __init__(self):
        print('游戏初始化')
    #1 创建游戏的窗口
    self.screen = pygame.display.set_mode(SCREEN_RECT.size)
    #2 创建一个游戏的时钟
    self.clock = pygame.time,Clock()
    #3 调用私有方法  精灵和精灵组的创建
    self.__create_sprites()
    '''创建所有的精灵和精灵组'''
    def __create_sprites(self):
        '''创建精灵组'''
        #背景组
        self.back_group = pygame.sptite.Group()
    def start_game(self):
        print('游戏开始')
        while True:
            # 1设置刷新频率(1秒刷新60帧)
            self.clock.tick(60)
            # 2 事件监听
            self.__event_handler()
            # 3 碰撞检测
            self.__check_collide()
            # 4 更新精灵组
            self.__update_sprites()
            # 5 更新屏幕刷新
            pygame.display.update()

    def __event_handler(self):
        '''事件监听'''
        #循环遍历 pygame包 event模块 get方法
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
    def __check_collide(self):
        '''碰撞检测'''
        pass
    def __update_sprites(self):
        '''精灵组的更新与绘制'''
        self.back_group.update()
        self.back_group.draw(self.screen)
    @staticmethod
    def __game_over():
        '''游戏结束'''
    print('游戏结束额')
    pygame.quit()
    exit()
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
    

