'''
王者荣耀正式版v1.0
1 功能提示，提示你这个系统有那些
2 开始业务逻辑
3 退出
'''
wzry_gnts = '王者荣耀系统功能提示'
print(wzry_gnts.center(30))
print('*'*50)
print('功能1:%s\n功能2:%s\n'%('注册','登录'))
print('*'*50)

#需要0一个列表来存储用户输入的帐号和密码
account_list = [{'name':'libai','passwd':'123456'}]

#要写两个按钮，这两个按钮就是两个函数
def login(zh='libai',mm='123456'):
    '''登录'''
    print('登录')
    for dic in account_list:
        if zh == dic['name']:
         
            if mm == dic['passwd']:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')


def register(zhanghao='shll',mima='123456'):
    '''注册'''
    print('注册')
    for dic in account_list:
        if zhanghao == dic['name']:
            print('你的帐号已经存在')
        else:
            #创建一个临时字典
            
            tempDic ={'name':zhanghao,'passwd':mima}
            try:
                acount_list.append(tempDic)
            except:
                print('出错了')
            print('注册成功')
            break
    
print('-'*50)
zhanghao = input('请输入帐号')
mima = input('请输入密码')
login(zhanghao,mima)
print('-'*50)
#register(zhanghao,mima)
