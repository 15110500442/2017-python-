#默认函数参数可以使用，  函数名._defaults_可以查看所有默认参数的值
def list_test(a,b=1):
    print((a+'')*b)
#用defaults来查看每个默认参数    
###list_test._defaults_#返回一个元组
print('-'*30)
list_test('hello')
print('-'*30)
list_test('woeld\n',8)
