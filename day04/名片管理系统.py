
print('1 添加一个新的用户')
print('2 删除用户名片')
print('3 查询一个名片')
print('4 退出系统')






card_infors = []
while True:
    num = int(input('请输入操作序号'))
    if num == 1:
        new_name = input('请输入新的名字')
        new_age = input('请输入新的年龄')
        new_num = input('请输入新的工号')
        new_gang_wei = input('请输入岗位')
        new_money = input('请输入薪水')
        new_date = input('请输入入职日期')
        new_infor= {'name':new_name,'age':new_age,'num':new_num,'gang_wei':new_gang_wei,'money':new_money,'date':new_date}
        card_infors.append(new_infor)
        for name in card_infors:
            print('*'*30)
            for k,v in name.items():
                print('%s:%s'%(k,v))
    elif num == 2:
        del_names = input("请输入删除的名片")
        for temp in card_infors:              #index = 0
            if del_names == temp('name'):       
                card_infors.remove(temp)       #del card_infors[index]
                print('删除成功，还有%s'%card_infors)    
                
    elif num == 3:
        name = input('请输入你要查询的名片')
        for names in card_infors:
            if name == names['name']:
                print('姓名:%s\t年龄:%s\t工号:%s\t岗位:%s\t薪水:%s\t入职日期:%s\n'%(names['name'],names['age'],names['num'],names['gang_wei'],names['money'],names['date']))
            
                
    elif num == 4:
        print('退出系统')
        break
    else:
        print('输入错误')

