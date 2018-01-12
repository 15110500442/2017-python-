def zhu_ce(account,password):
    f = open('account.txt','w+')#创建一个用于储存帐号的文件
    f.write(account)
    f.close()
    f2 = open('password.txt','w+')
    f2.write(password)
    print('注册成功')
    f2.close()
#登录模式
def deng_lu(account,password):
    f = open('account.txt','r')
    b = f.readlines()
    f2 = open('password.txt','r')
    c = f2.readlines()
    if account == b[0]:
        if password == c[0]:
            print('登录成功')
        else:
            print('密码输入错误')
    else:
        print('帐号不存在')
        break
    f.close()
    f2.close()
while True:
    num = int(input('1是注册,2是登录'))
    account = input('请输入帐号')
    password = input('请输入密码')
    if num == 1:
        zhu_ce(account,password)
    elif num == 2:
        deng_lu(account,password)
        
