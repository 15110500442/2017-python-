zhan_hao_and_mi_ma = {}
def wzry_deng_lu(zh,mm):
    for zh_1,mm_1 in zhang_hao_and_mi_ma.items():
        if zh == zh_1:
            if mm == mm_1:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号错误')
    print('登录成功')  
def wzry_zhuz_ce():
    zhanghao = input('请输入帐号')
    mima = input('请输入密码')
    if zhanghao in zhang_hao_and_mi_ma.values():
        print('对不起，帐号已经存在')
    else:
        zhang_hao_and_mi_ma['zhangz_hao']=zhanghao
        zhang_hao_and_mi_ma['mi_ma']=mima
        print('注册成功')
        wzry_deng_lu(zhanghao,mima)
    print('2 注册按钮')


wzry_deng_lu(5555,55555555)
wzry_zhu_ce()
