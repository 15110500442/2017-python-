def one(a):
    print('修改前:',a)
    a+=1
    print('这是修改后的',a)
    return a
a = 6
print('函数内部操作后的a:',one(a))
print('函数外部的变量a为:',a)
