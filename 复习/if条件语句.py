#一  if条件语句
#1 一个最简单的if语句
heroes = [
            '安其拉','李白','杨戩','貂蝉','孙悟空'
            ] 
for hero in heroes:
    if hero =='李白':
        print('你要选的英雄超级厉害的')
    else:
        print('你选的英雄一般般厉害')


#if 条件判断的内容分类
#  文本内容相同
hero = 'libai'
if hero == 'libai':
    print('您选择的英雄是超级大嘴炮:李白')
if hero == 'LIBAI':
    print('您选择的英雄是名字大写的超级大嘴炮:李白')

#文本内容不相同
hero = '老夫子'
if hero != '后羿':
    print(
            '恭喜你,这局你已经赢了一大半了'
            )



#比较数字
age = 11
if age <= 12:
    print('尊敬的小玩家,您每日的游戏时间只有1小时')


#多个条件并列
liucuihua = 18
wangergou = 22
if (liucuihua > 12 and wangergou > 12):
    print('恭喜刘翠花和王二够能够组队玩一天')

#列表中是否包含特定值
heroes = ['安其拉','李白','杨戩','貂蝉','孙悟空']
hero = '后羿'
if hero in heroes:
    print('队伍中有后羿,赶紧题掉他')
else:
    print('后羿不在队伍中,能赢')


#字典
#1 一个简单的英雄子典
libai = {'姓名':'李白','性别':'男'}
print(libai)



#向字典中添加内容
libai={"姓名":"李白","性别":"男"}
print(libai)
libai["名句"]="努力有用的话还要天才干甚？"
print(libai)


#修改字典中的内容
libai={"姓名":"李白","性别":"男"}
print(libai)
libai["性别"]="女" #修改性别对应的值
print(libai)

#删除字典中的内容
libai={"姓名":"李白","性别":"男"}
print(libai)
del libai["性别"] #删除一个键值对，只需要指定键就可以了
print(libai)




#遍历字典
songfen={"马花藤":"安其拉","天善梁总":"孙悟空","酸菜馆子刘翠花":"貂蝉","村口铁匠王二狗":"吕布","小菜鸡郑开州":"后羿"}
print(songfen)

#1 遍历字典中的所有键
songfen={"马花藤":"安其拉","天善梁总":"孙悟空","酸菜馆子刘翠花":"貂蝉","村口铁匠王二狗":"吕布","小菜鸡郑开州":"后羿"}
for key in songfen.keys(): #取出字典中的玩家名称
    print(key)



#遍历字典中的所有键值对
songfen={"马花藤":"安其拉","天善梁总":"孙悟空","酸菜馆子刘翠花":"貂蝉","村口铁匠王二狗":"吕布","小菜鸡郑开州":"后羿"}
for key,value in songfen.items(): #取出字典中的玩家名称
    print(key,value)



# 2 字典嵌套
songfen={"玩家名称":["马花藤","天善梁总","酸菜馆子刘翠花","村口铁匠王二狗","小菜鸡郑开州"],"所选英雄":["安其拉","孙悟空","貂蝉","吕布","后羿"]}
songfen



#2 吧这几个放在一个列表里面
libai={"姓名":"李白","性别":"男"}
diaochan={"姓名":"貂蝉","性别":"女"}
direnjie={
            "姓名":"狄仁杰","性别":"男"
            }
heroes=[libai,diaochan,direnjie]
print(heroes)


