#入门语句
print('欢迎来到召唤师峡谷！')

#使用变量
msg = '欢迎来到召唤师峡谷！'
print(msg)

#字符串大小写变换（仅针对英文）
name = 'wangzherongyao'
print(name.title()) #首字母大写
print(name.upper()) #全部字母大写
print(name.lower()) #全部字母小写

# 合并（拼接）字符串
first_name = '郑'
last_name = '开州'
        full_name = first_name+''+last_name
print(full_name)
print("尊敬的召唤师:"+full_name+",欢迎来到召唤师峡谷！")

#制表符和换行符的使用
print('欢迎来到召唤师峡谷!')
print('\t欢迎来到召唤师峡谷!')
print('\n欢迎来到召唤师峡谷!')

#删除字符串两端的空白
msg = '   努力有用的话还要天才干什么?    '
print(msg)
msg = msg.strip()
print(msg)


#数字变量的正确文本显示
num = 2
msg = ("尊敬的召唤师,您在这局对战中的综合评分位于第"+str(num)+"位!")
print(msg)




#二　　列表的元素基础
#1 最基础的列表
heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)

#访问列表中的元素
heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
print(heroes[0])
print(heroes[1])


#修改列表元素

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
heroes[0] = '狄仁杰'
print(heroes)



#在列表末尾新增夹元素

heroes = ['安其拉','李白','杨戩','貂蝉']
print(heroes)
heroes.append('兰陵王')
print(heroes)




#在列表中指定位置插入元素

heroes = ['安其拉','李白','杨戩','貂蝉']
heroes.insert(0,'兰陵王')
print(heroes)



#从列表中删除元素
#1 概念删除

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
del heroes[0]
print(heroes)



#2 可调用删除

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
tail = heroes.pop()
print(heroes)
print(tail)


#3 定值删除

heroes = ['安其拉','李白','杨戩','后羿','貂蝉']
print(heroes)
heroes.remove('后羿')
print(heroes)


#列表排序
#1 概念排序

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
heroes.sort
print(heroes)

#2 反向排序

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
heroes.sort(reverse=True)
print(heroes)
#3 临时排序

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
print(sorted(heroes))
print(heroes)



#反向　排序列表元素

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
print(heroes)
heroes.reverse()
print(heroes)


#计算列表中元素的计数项

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
len(heroes)




#三　列表的进一步操作
#1 遍历整个列表

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
for a in heroes:
    print('您的队伍中有此英雄:'+a)

#在循环中加入一些废话

heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
for a in heroes:
    print(a+"是一个十分优秀的英雄!"+"\n")



#数字列表
# 使用range函数
for a in range(1,5):
    print(a)



#创建一个最简单的数字列表
num = list(range(1,6))
print(num)

#从外部添加数字到数字列表（计算平方值）
pingfangji = []
for shuzi in range(1,11):
    pingfang = shuzi ** 2
    pingfangji.append(pingfang)
print(pingfangji)
