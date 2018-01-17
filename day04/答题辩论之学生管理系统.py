print('*'*40)
print('1 添加一个学生用户')
print('2 删除一个学生用户')
print('3 修改一个学生用户')
print('4 查询学生用户资料')
print('5 退出学生管理系统')
print('*'*40)
names = []
while True:
    number = input('请输入序号')
#添加学生信息:
    if number == 1:
        new_name = input('请输入姓名')
        new_age = input('请输入年龄')
        new_xueid = input('请输入学号')
        new_class = input('请输入班级')
        new_zhuan_ye = input('请输入专业')
        new_tel = input('请输入电话')
        new_infor = {'姓名':new_name,'年龄':new_age,'学号':new_xueid,'班级':new_class,'专业':new_zhuan_ye,'电话':new_tel}
        names.append(new_infor)
        for name in names:
            print('*'*30)
            for k,v in name.items():
                print('%s:%s'%(k,v))
    
