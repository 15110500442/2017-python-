sheng = ['山西':'河北']
shi = ['忻州':'北京']
xian = ['定襄':'大兴']
a = {'省':sheng,'市':shi,'县':xian}
test = input('请输入你要找的类型')
print(a.get(test))
