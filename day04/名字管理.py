print('*'*50)
print('名字关系管理系统')
print('1 添加一个新的名字')
print('2 删除一个名字')
print('3 修改一个名字')
print('4 查询一个名字')
print('*'*50)

names = []
while True:
    num = int(input('请在此输入你需要的功能'))
    print('num=%d'%num)
    if num==1:
        name = input('请输入要添加的用户')
        names.append(name)
        print('添加成功，当前的名字一共有%s'%names)
    elif num==2:
        name = input("请输入要删除的用户")
        names.remove(name)
        print('删除成功，当前的名字还有%s'%names)
    elif num==3:
        name_user = input('请输入你要修改的用户')
        
        if name in names:
            print('name_user=%s'%name_user)

            nameIndex = names.index(name_user)
            names[nameIndex] = input('请输入你要修改的用户')
            print('修改成功，当前的用户有%s'%names)
    elif num==4:
        find_name = input('请输入查询名字')
        if find_name in names:
            print('查到你要找的人')
        else:
            print('差无此人')
    elif num==5:
        
        break
    else:
        print('输入错误，请重新输入')



