#第一种可变长参数：
def demo(*e):
    print(e)
demo(1,2,3)
print('-'*40)
demo(1,2,3,4,6)
print('-'*40)
#第二种参数：
def demo2(**e):#k是自定义什么都可以
    for dic in e.items():
        print('dic')
demo2(x=1,y=2,z=3,j=4)
