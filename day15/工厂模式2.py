class Car(object):
    def move(self):
        print('车移动')
    def music(self):
        print('听音乐')
    def stop(self):
        print('停车')
#销售店的类
class CarStroe(object):
    def order(self):
        self.car = Car()#找一辆车
        self.car.move()
        self.car.stop()
buy_car = CarStroe()
buy_car.order()
