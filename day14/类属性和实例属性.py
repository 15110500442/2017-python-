'''
class People(object):
    yanjing = '黑色'
    __jiying = 'X'
    def __init__(self):
        self.name = '张三'
        self.age = 15
p = People()
print(p.name)#这是通过实例对象来调用实例属性
print(People.yanjing)#这是通过类来调用类属性
'''



class People(object):
    address = '山西'#类属性
    num = 0#查看被调用了几次
    def __init__(self):
        self.name = '史金磊'#实例(对象)属性
        self.age = 24#实例属性
sjl = People()
sjl.age = 30#实例属性
print(sjl.age)
print(sjl.name)#通过对想来调用实例属型
print(sjl.address)#通过实例对象来调用类属性
print('------------------------------------')
People.num = People.num+1

sxl = People()
sxl.age = 17
sxl.name = '史鑫磊'
print(sxl.age)
People.num = People.num+1
print(sxl.name)#通过对象调用对象属性（通过实例调实例属性）
print(sxl.address)#通过实例对象来调用类属性
print('------------------------------')
print(People.address)#通过类来调用类属性
print(People.num)
