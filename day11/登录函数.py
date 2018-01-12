#注册的函数
def register(account,password):
    #打开文件，以读的方式
    f = open('account.txt','r')
    account_list = f.readlines()
    #本地的帐号我已经取出来了，接下来呢？我们需要去判断，本地的帐号有没有
    lenght = len(account.list)
    f.close()
    if lenght == 0:
        print('可以创建帐号')
        f = open('account.txt','w')
        f.write(account)
        f.close()
    else:
        names = []
        for name in account_list:
            names.append(name.rstrip())
        if account in names:
            print('帐号已经存在')
        else:
            f = open('account.txt','a')
            account = '\n'+account
       















































