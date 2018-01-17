def asu_shu(a,b):
    a1 = a
    a2 = b
    a3 = a+b
    return a3
def bsu_shu(a):
    a1 = a
    a2 = asu_shu(10,20)-a
    return {'name1':a1,'name3':a2}
sum=bsu_shu(10)
print('最后输入的是%s最后结果是%s'%(sum['name1'],sum['name3']))
