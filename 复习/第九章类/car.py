class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        '''
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def get_descriptive_name(self):
        '''返回整洁的描述姓信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        '''打印一条指出汽车里程的信息'''
        print("This car has " + str(self.odometer_reading) + "miles on it.")
    def increment_odometer(self,miles):
        '''将里程表读数增加指定的量'''
my_new_car = Car('奥迪','TT',2018)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23#直接修改属性的值
my_new_car.update_odometer(23)#  通过方法来修改
my_new_car.read_odometer()
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


print('---------------------------------------------')

print('-------------继承---------------')

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        '''
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def get_descriptive_name(self):
        '''返回整洁的描述姓信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        '''打印一条指出汽车里程的信息'''
        print("This car has " + str(self.odometer_reading) + "miles on it.")
    def increment_odometer(self,miles):
        '''将里程表读数增加指定的量'''

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        '''
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def get_descriptive_name(self):
        '''返回整洁的描述姓信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        '''打印一条指出汽车里程的信息'''
        print("This car has " + str(self.odometer_reading) + "miles on it.")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    '''一次模拟的电动汽车电瓶的简单尝试'''
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        '''将打印一条描述电瓶容量的消息'''
        print('This car has a ' + str(self.battery_size) + '-kwh battery.')
    def get_range(self):
        '''打印一条信息,指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.batteryz_size == 85:
            range =270
        message = "This car can go aoorocumately" + str(range)
        message += 'miles on a full charge'
        print(message)

class ElectricCar(Car):
    '''电动车的独特之处'''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        '''电瓶汽车没有邮箱'''
        print("This car doesn't need a gas tans!")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()




