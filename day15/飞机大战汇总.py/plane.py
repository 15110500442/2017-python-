import pygame
class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵的基类'''
    def __init__(self,image_name,speed = 1):
        #先调用父类的初始化方法
        super().__init__()
        #加载图像
        self.image = pygame.image.load(image_name)
        #设置尺寸
        self.rect = self.image.get_rect()
        #记录速度
        self.speed = speed
    def update(self,*args):
        #设置在垂直方向移动
        self.rect.y += self.speed
class Hero(GameSprite):
    '''英雄精灵'''
    def __init__(self):
        super().__init__('/mnt/images/me1.png',0)
        #设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
    def update(self):
         #飞机水平移动
         self.rect.x += self.speed
         #获取用户安键
         keys_pressed = pygame.key.get_pressed()
         if keys_pressed[pygame.K_RIGHT]:
             self.hero.speen = 2
         elif keys_pressed[pygame.K_RIGHT]:

             self.hero.speen = -2
         else:
             self.hero_speed = 0
     
             

