#人类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None
    def __str__(self):
        return self.name + '剩余的血量为:' + str(self.xue)
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)
    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)
    def naqiang(self,qiang):
        self.qiang = qiang
    def kaiqiang(self,diren):
        self.qiang.she(diren)
    def diaoxue(self,shashangli):
        self.xue -= shashangli
#弹夹类
class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.ronglist = []
    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.ronglist)) + '/' + str(self.rongliang)
    def baocunzidan(self,zidan):
        if len(str(self.rongliang)) < self.rongliang:
            self.ronglist.append(zidan)
    def chuzidan(self):
        if len(self.ronglist) > 0:
            zidan = self.ronglist[-1]
            self.ronglist.pop()
            return zidan
        else:
            return None
#子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli
    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)
#枪类
class Qiang:
    def __init__(self):
        self.danjia = None
    def __str__(self):
        if self.danjia:
            return "枪当前有弹夹"
        else:
            return '枪没有弹夹'
    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia
    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print('没有子弹了，放了空枪...')
#创建一个人对象
laowang = Ren('老王')
#创建一个弹夹
danjia = Danjia(20)
print(danjia)
#循环的方式创建一颗子弹，然后让老王吧这颗子弹压入弹夹中
i = 0
while i<10:
    zidan = Zidan(33.3)
    laowang.anzidan(danjia,zidan)
    i+=1
#测试一下 安装完子弹后，弹夹中的信息
print(danjia)
#创建一个枪对象
qiang = Qiang()
print(qiang)
#让老王把弹夹连接到枪中
laowang.andanjia(qiang,danjia)
print(qiang)
#创建一个敌人
diren = Ren('敌人')
print(diren)
#让老王拿起枪
laowang.naqiang(qiang)
#老王开枪射敌人
laowang.kaiqiang(diren)
print(diren)
print(danjia)
laowang.kaiqiang(diren)
print(diren)
print(danjia)
laowang.kaiqiang(diren)
print(diren)
print(danjia)
