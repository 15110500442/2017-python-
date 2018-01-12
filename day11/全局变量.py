#先定义一个全局变量
#a = 3
#定义一个函数
def test():
    global a
    a = 1
    print(a)
def test2():
    #a = 4
    print(a)
test()
print('-'*30)
test2()
print('-'*30)
print(a)

