#阿里巴巴员工管理系通
print('1添加信息')
print('2查询信息')
print('3删除信息')
print('4退出系统')
xi_tong = []
while True:
    num = int(input('请输入操作序号'))
 
    if num == 1:
        name = input('请输入你的名字')
        age = input('请输入你的年龄')
        num = input('请输入你的工号')
        gang_wei = input('请输入你的工作岗位')
        money = input('请输入你的薪水')
        date = input('请输入你的入职日期')
        xin_xi = {'name':name,'age':age,'mun':num,'gangwei':gang_wei,'xinshui':money,'ruzhiriqi':date}
        xi_tong.append(xin_xi)
        for name in xin_xi:
            print('*'*30)
            for k,v in name.items():
                print('%s:%s'%(k,v))
    elif num == 2:
        name = input('请输入你要查询的信息')
        for names in xi_tong:
            if name == names['name']:
                print('姓名%s\t年龄%s\t工号%s\t工作岗位%s\t薪水%s\t入职日期%s\n'%(names['name'],names['age'],names['num'],namas['gang_wei'],names['money'],names['date']))
    elif num == 3:
        del_name = input('请输入你要删除的名字')
        for temp in xi_tong:
            if del_name == temp('name'):
                xi_tong.remove(temp)
                print('删除成功，还有%s'%xi_tong)


    elif num == 4:
        print('退出系统')
        break
    else:
        print('输入错误')
