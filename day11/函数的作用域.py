a = 3
def test1():
    global a
    a = 1
    print(a)
def test2():
    a = 2#临时变量
    print(a)
test1()
print('-'*30)
test2()
print('-'*30)
print(a)
