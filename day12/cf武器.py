class Weapon:#武器
    def __init__(self,newname):
        self.name = newname
    def sheji(self):
        print(self.name,'射击')
    def murder(self):
        print(self.name,'杀人')
hws_weapon = Weapon('黑武士:')
hws_weapon.sheji()
hws_weapon.murder()
hws_weapon.color = '黑色'
hws_weapon.rongliang = '35/105'
hws_weapon.type = '步枪'
print('黑武士的属性有:\n颜色:%s\n弹夹容量:%s\n类型:%s'%(hws_weapon.color,hws_weapon.rongliang,hws_weapon.type))
print('-'*20)
ss_weapon = Weapon('死神:')
ss_weapon.sheji()
ss_weapon.murder()
ss_weapon.color = '白色'
ss_weapon.rongliang = '36/108'
ss_weapon.type = '步枪'
print('死神的属性有:\n颜色:%s\n弹夹容量:%s\n类型:%s'%(ss_weapon.color,ss_weapon.rongliang,ss_weapon.type))
print('-'*20)
ms_weapon = Weapon('毛瑟:')
ms_weapon.sheji()
ms_weapon.murder()
ms_weapon.color = '金色'
ms_weapon.rongliang = '18/36'
ms_weapon.type = '手枪'
print('毛瑟的属性有:\n颜色:%s\n弹夹容量:%s\n类型:%s'%(ms_weapon.color,ms_weapon.rongliang,ms_weapon.type))
print('-'*20)
hm_weapon = Weapon('毁灭:')
hm_weapon.sheji()
hm_weapon.murder()
hm_weapon.color = '黑色'
hm_weapon.rongliang = '10/20'
hm_weapon.type = '狙击枪'
print('毁灭的属性有:\n颜色:%s\n弹夹容量:%s\n类型:%s'%(hm_weapon.color,hm_weapon.rongliang,hm_weapon.type))
print('-'*20)
RPK_weapon = Weapon('RPK:')
RPK_weapon.sheji()
RPK_weapon.murder()
RPK_weapon.color = '金色'
RPK_weapon.rongliang = '110/165'
RPK_weapon.type = '机枪'
print('RPK的属性有:\n颜色:%s\n弹夹容量:%s\n类型:%s'%(RPK_weapon.color,RPK_weapon.rongliang,RPK_weapon.type))
        
