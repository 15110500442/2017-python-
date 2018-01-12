# 使用pygame  我们要先导入这个包
import pygame
from plane_sprites import *

class PlaneGame(object):
    '''飞机大战主游戏'''
    
    
    def __init__(self):
        print('游戏初始化')
        #创建游戏窗口  pygame.display.set_mode  创建游戏窗口  需要传宽和高
        #.size 取宽高    x取x轴的值   y取y轴的值
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        #创建游戏时钟  pygame.time,Clock() 会给我们返回一个时钟对象
        self.clock = pygame.time.Clock()
        #创建私有方法  里面的创建精灵和精灵组
        self.__create_sprites()
        #敌机常量              
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        #发射子弹
        #pygame.time.set_timer(HERO_FIRE_EVENT,200)
    def start_game(self):
        print('开始游戏')
        while True:
            # 设置帧率
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 碰撞检测、
            self.__check_collide()
            # 更新精灵.K_RIGHT:
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()
    
    
    def __create_sprites(self):
        '''创建精灵和精灵组'''
         #pygame.sprite.Group()可以创建一个精灵组
        #  背景精灵组
        bg1 = Backgroup('/mnt/images/01535957bea52b0000018c1b79aad8.jpg@1280w_1l_2o_100sh.jpg')
        bg2 = Backgroup('/mnt/images/01535957bea52b0000018c1b79aad8.jpg@1280w_1l_2o_100sh.jpg')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #  敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #  英雄精灵组
        self.hero = Hero()
        self.hero2 = Hero()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero2)
    
    
    def __event_handler(self):
        '''事件监听的方法'''
       # pygame.event.get()获取监听事件的列表
       # 获取完列表之后 写了一个for循环  循环这个列表
        for event in pygame.event.get():
            print(event)
             #当列表里面pygame.QUIT这个值的时候  说明用户
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                self.hero2.fire()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.hero.fire()
                elif event.type == 271:
                    self.hero2.fire()
        keys_pressed = pygame.key.get_pressed()
       
        if keys_pressed[100]:
            self.hero2.speed = 2               
           
        elif keys_pressed[97]:
            self.hero2.speed = -2
        elif keys_pressed[271]:
            self.hero.fire()
        elif keys_pressed[pygame.K_SPACE]:
            self.hero2.fire()
        else:
            self.hero2.speed = 0
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        #elif keys_pressed[271]:
        #    self.hero.fire()
        #elif keys_pressed[pygame.K_SPACE]:
        #    self.hero2.fire()
        else:
            self.hero.speed = 0


    def __check_collide(self):
        '''碰撞检测'''
        
        #1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group, True, True)
        pygame.sprite.groupcollide(self.hero2.bullets,self.enemy_group, True, True)

        # 2. 敌机撞毁英雄1
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        enemies1 = pygame.sprite.spritecollide(self.hero2, self.enemy_group, True)

        # 判断列表时候有内容1
        if len(enemies) > 0 or len(enemies1):

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    
    
    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            #更新精灵组里面所有精灵的位置
            group.update()
            #绘制到屏幕上
            group.draw(self.screen)
            self.hero_group.update()
            self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        
        self.hero2.bullets.update()
        self.hero2.bullets.draw(self.screen)
             #静态方法
    @staticmethod
    
    
    def __game_over():
        '''游戏结束'''
        print('游戏结束')
        pygame.quit()
        exit()
        pass
        

#一般情况下  比如有一个场景   测试
if __name__ == '__main__':
    '''创建游戏对象'''
    game = PlaneGame()
    '''调用开始游戏的方法'''
    game.start_game()
