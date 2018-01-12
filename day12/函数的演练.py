name = '小明'
#解释器知道这里定义一个函数
def say_hello():
    print('hello 1')
    print('hello 2')
    print('hello 3')
print(name)
#只有在调用函数的时候，之前定义的函数才会执行
#函数执行完成后，会重新回到之前的程序中执行后续的代码
say_hello()
print(name)
