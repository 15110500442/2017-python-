account_passwd = []
list_account = []
def zhu_ce():
    name = input('请输入你要注册的帐号')
    for dic in account_passwd:
        list_account.append(dic['name'])
    if name in list_account:
        print('你的账户已经存在')
    elif name not in list_account:
        passwd = input('请输入你的注册密码')
        ling_shi = {}
        ling_shi['name'] = name
        ling_shi['passwd'] = passwd
        account_passwd.append(ling_shi)
        print('注册成功')
        print(account_passwd)
        deng_lu = input('是否登录')
        if deng_lu == '是':
            print('帐号已经登录过')
        else:
            print('登录')
zhu_ce()
