#修改全局变量
a = [1]
def quanju():
    b = 2
    a.append(b)
    print(b)
def quanju2():
    #b = 2
    print(b)
quanju(a)
quanju2(a)
print(a)

