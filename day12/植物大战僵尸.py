class Plants:

    def fyg(self):
        print('放阳光')
    def fa_pao(self):
        print('发炮')
    def yao_tou(self):
        print('摇头')
    def zu_dang(self):
        print('阻挡')
class Zombie: 
    def walk(self):
        print('走')
    def pao(self):
        print('跑')
    def tiao(self):
        print('跳')
    def chi(self):
        print('吃')
    def death(self):
        print('死')

sunflower_plants = Plants()
sunflower_plants.name = '向日葵'
sunflower_plants.clocr = '绿色'
sunflower_plants.height = 150
sunflower_plants.price = 50
sunflower_plants.gongji = 1800
sunflower_plants.naijiu = 300
print('%s的属性有:\n颜色:%s\n身高:%d\n攻击:%d\n耐久力:%d'%(sunflower_plants.name,sunflower_plants.clocr,sunflower_plants.height,sunflower_plants.gongji,sunflower_plants.naijiu))
print('%s的方法行为有:'%sunflower_plants.name)
sunflower_plants.fyg()

print('-'*20)
pea_plants = Plants()
pea_plants.name = '豌豆'
pea_plants.clocr = '绿色'
pea_plants.hair_style = '草花模型'
pea_plants.xue = 500
pea_plants.gongji = 20
pea_plants.naijiu = 300
print('%s的属性有:\n颜色:%s\n发型:%s\n血量:%d\n攻击:%d\n耐久力:%d'%(pea_plants.name,pea_plants.clocr,pea_plants.hair_style,pea_plants.xue,pea_plants.gongji,pea_plants.naijiu))
print('%s的方法行为有:'%pea_plants.name)
pea_plants.fa_pao()
pea_plants.yao_tou()
print('-'*20)
nut_plants = Plants()
nut_plants.name = '坚果'
nut_plants.naijiu = 4000
nut_plants.lq_time = '30/s'
print('%s的属性有:\n耐久力:%d\n冷却时间:%s'%(nut_plants.name,nut_plants.naijiu,nut_plants.lq_time))
print('%s的方法行为有:'%nut_plants.name)
nut_plants.zu_dang()
print('-'*20)
zombie = Zombie()
zombie.name = '僵尸'
zombie.colcr = '蓝色'
zombie.xue = 500
zombie.type = '旗帜僵尸 塑料僵尸 撑杆僵尸'
zombie.sudo = '旗帜僵尸:低 塑料僵尸:中等 撑杆僵尸:快'
print('%s的属性有:\n颜色:%s\n血量:%d\n类型:%s\n速度:%s'%(zombie.name,zombie.colcr,zombie.xue,zombie.type,zombie.sudo))
print('%s的方法行为有:'%zombie.name)
zombie.walk()
zombie.pao()
zombie.tiao()
zombie.chi()
zombie.death()
