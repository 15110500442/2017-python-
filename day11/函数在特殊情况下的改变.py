#修改实参：
def name(a):
    a[0] = a[0]+1
    return a
a = [2]#实参的列表
print(name(a))
print(a)#输出的是实参值

print('-'*30)


def name2(a,v):#为列表添加元素
    a.append(v)
    return a  #返回到a值
b = [5]
print(name2(b,18))
print(b)
print('-'*30)


def name3(c):#修改字典的元素或者是为字典增加元素
    c['diqu'] = '太原'
d = {'sheng':'山西','diqu':'太原'}
print(d)


