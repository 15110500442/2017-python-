'''
学员管理系统v1.0
功能有 添加  删除  修改  查询  退出
使用列表
添加
删除
修改
查询
退出(每一个功能都要有一个函数)
'''
#定以一个空列表来装信息
he_zi = []
#定义一个函数  这个函数什么爷不做，就是输出横线
def printline():
    print('*'*50)
#1 添加
def tian_jia():
    name = input('请输入姓名')
    age = input('请输入年龄')
    num = input('请输入学号')
    ban_ji = input('请输入班级')
    zhuan_ye = input('请输入专业')
    addr = input('请输入地址')

    xin_xi = {'姓名':name,'年龄':age,'学号':num,'班级':ban_ji,'专业':zhuan_ye,'地址':addr}
    he_zi.append(xin_xi)
    printline()
    print('现在有的学生是%s'%he_zi)
    printline()
#2 删除
def shan_chu():
    name = input('请输入你要删除的人')
    count = 0 
    for dic in he_zi:
        if dic['姓名'] == name:
            del he_zi[count]
        else:
            count+=1
    print('此时还有%s'%he_zi)
    printline()

def xiu_gai():
    name = input('请输入你要修改的名字')
    count = 0
    for dic in he_zi:
        if dic['姓名']==name:
            he_zi[count]['姓名']=input('请输入姓名')
            he_zi[count]['年龄']=input('请输入年龄')
            he_zi[count]['学号']=input('请输入学号')
            he_zi[count]['班级']=input('请输入班级')
            he_zi[count]['专业']=input('请输入专业')
            he_zi[count]['地址']=input('请输入地址')
        else:
            count+=1
    printline()
    print('现在还有那些%s'%he_zi)
    printline()

            

def cha_xun():
    for dic in he_zi:
        print('姓名:%s\t年龄:%s\t学号:%s\t班级:%s\t专业:%s\t地址:%s\t'%(dic['姓名'],dic['年龄'],dic['学号'],dic['班级'],dic['专业'],dic['地址']))
def tui_chu():
    pass
#调用函数
tian_jia()
tian_jia()
tian_jia()
shan_chu()
xiu_gai()
cha_xun()
