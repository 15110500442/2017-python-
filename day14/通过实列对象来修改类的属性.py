class People(object):
    country = 'china'#类属性
print(People.country)#输出类的属性
p = People()
p.country = '中国'
print(p.country)#实例属性会屏蔽掉同名类的属性
print(People.country)#也可以通过类来调用类属性
del p.country #删除实例属性
print(p.country)
