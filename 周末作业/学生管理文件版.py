#学生管理系统(文件版)
print('1 注册帐号')
print('2 登录帐号')
print('3 增加信息')
print('4 删除信息')
print('5 修改信息')
print('6 查询信息')
print('7 退出系统')
def register(account,passwd):
   account = open('account.txt','r')
   passwd = open('passwd.txt','r')
   account_list = account.readlines()
   passwd_list = passwd.readlines()
   lenght = len(account_list)
   lenfht = len(passwd_list)
   account.close()
   passwd.close()
   if lenght == 0:
       print('可以创建帐号')
       account = open('account.txt','w')
       account.write(account)
       account.close
   else:
       names = []
       for name in account_list:
           naems.append(name.rstrip())
       if account in names:
           print(')
