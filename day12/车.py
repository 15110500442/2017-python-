class Car:
    def move(self):
        print('移动')
#创建一个实列
    def zuo(self):
        print('坐')
    def toot(self):
        print('叫')
red_car = Car()
red_car.move()
print('-'*20)
blue_car = Car()
blue_car.zuo()
print('-'*20)
yellow_car = Car()
yellow_car.move()
yellow_car.zuo()
yellow_car.toot()
