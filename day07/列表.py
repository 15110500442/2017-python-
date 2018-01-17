a = ['1','2','3','5']
'''
b = ['7','8']

a.extend(b)
print(a)
'''
'''
print('9没有出现之前的是：%s'%b)
b.insert(1,'9')
print('三人行:%s'%b)
b.insert(0,'6')
print('一家四口%s'%b)
'''
'''
b[1] = '1111'
print(b)
'''
shi = input("请输入你要找的名字")
if shi in a:
    print("%s在"%shi)
else:
    print("不再")
