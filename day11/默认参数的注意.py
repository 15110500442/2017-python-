#在多次调用上会出现的细节问题 
def demo(a,b=[]):
    b.append(a)
    return b
print(demo('5',[1,2,3,4]))
print('-'*30)
print(demo('aaa',['a','b']))
print('-'*30)
print(demo('a'))
print('-'*30)
print(demo('b'))
print('-'*30)
print(demo('c'))


print('----'*20)

#解决出现叠加的情况
def demo2(a,b=[]):
    if b is None:#None是空值的意思
        b=[]
    b.append(a)
    return b
print(demo2('6',[1,2,3,4,5,6,7,8,9]))
print('-'*30)
print(demo2('aaa',['a','b']))
print('-'*30)
print(demo2('a'))
print('-'*30)
print(demo2('b'))
print('-'*30)
print(demo2('c'))
print('-'*30)
print('-'*30)
print('-'*30)


