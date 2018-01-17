'''定义类'''
class Dog:
    def walk(self):
        print('走')
    def drink(self):
        print('喝水')
    def tian(self):
        print('舔')
    def niao(self):
        print('尿尿')
    
#创建一个对象
sugar = Dog()
sugar.name = '冰糖'
print('那只叫%s的狗狗正在'%sugar.name)
sugar.walk()
sugar.drink()
sugar.tian()
sugar.niao()
sugar.name = 'jj'

print('那只叫%s的狗狗正在'%sugar.name)
sugar.walk()
sugar.drink()
#print('那只叫%s的狗狗'%sugar.name)
