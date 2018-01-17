#学生的管理系统
def tianjia():
    name = input('请输入你的姓名')
    age = int(input('请输入年龄'))
    sex = input('请输入性别')
    student = str({'姓名':name,'年龄':age,'性别':sex})
    tian_jia = open('学生信息','r')
    student_list = tian_jia.readlines()
    lenght = len(student_list)
    tian_jia.close()
    if lenght == 0:
        print('可以添加')
        tian_jia = open('学生信息','w')
        tian_jia.write(student)
        tian_jia.close()
    else:
        xin_xi = []
        for name in student_list:
            xin_xi.append(name)
        if student in xin_xi:
            print('信息已经存在')
        else:
            tianjia = open('学生信息','a')
            student = '\n'+student
            tianjia.write(student)
            tianjia.close()
            student = student_list

student = int(input('1 添加 2 删除 3 修改 4 查询 5 退出'))
tianjia()


  
    
