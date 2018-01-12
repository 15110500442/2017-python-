import pygame
from plan_sprite import *
class PlaneGame(object):
    '''飞机大战的主程序类'''
    def __init__(self):
        '''初始化游戏'''
        #1 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2 游戏时钟
        self.clock = pygame.time.Clock()
        #3 调b用私有方法
        self.__creat_sprites()
    
    def start_game(self):
        print('开始游戏')
        while True:
            #1 设置帧率
            self.clock.tick(60)
            #2 事件监听
            self.__event_hander()
            #3 碰撞检测
            self.__check_collide()
            #4 更新精灵组
            self.__update_sprites()
            #5 更新屏幕显示
            pygame.display.update()
    def __creat_sprites(self):
        '''这是创建精灵（背景  飞机  敌人）的函数'''
        #创建背景精灵组
        bg1 = Backgroup('/home/shijinlei/桌面/python基础/day15/飞机大战汇总.py/image/images/background.png')
        
        bg2 = Backgroup('/home/shijinlei/桌面/python基础/day15/飞机大战汇总.py/image/images/background.png')
        bg2.rect.y = -bg2.rect.height


        #1  背景组
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #2 敌机组
        self.enemy_group = pygame.sprite.Group()
        #3 英雄组
        self.hero_group = pygame.sprite.Group()
    def __event_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
        pass
    def __check_collide(self):
        '''碰撞检测'''
        pass
    def __update_sprites(self):
        for group in [self.back_group,self.enemy_group,self.hero_group]:
            group.update()
            group.draw(self.screen)
    @staticmethod
    def __game_over():
        '''游戏结束'''
        print('游戏结束')
        pygame.quit()
        exit()

        '''刷新精灵组'''

if __name__ =='__main__':
    #创建游戏
    game = PlaneGame()
    #开始游戏
    game.start_game()

