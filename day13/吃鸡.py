class Ren:
   
    def __inti__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None
    
    def __str__(self):
        return self.name + '剩余的血:' + str(self.xue)
     
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andianjia(self,qiang,danjia):
        qiang.lianjiezidan(zidan)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue -= shashangli

class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongnaList = []
    def __str__(self):
        return '弹夹当前的子弹数量为:' + str(len(self.rongnaList)) + '/' + str(self.rongliang)
    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongList.append(zidan)
    
    def chuzidan(self):
        if len(self.rongnaList) > 0:
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None
class Zidan:
    def __init__(self,shangshali):
        self.shashangli = shashangli
    def shanghai(self,diren):
        diren.diaoxue(self,shashangli)

class Qiang:
    def __init__(self):
         self.danjia = None
    def __str__(self):
        if self.danjia:
            return '枪当前有弹夹'
        else:
            return '枪没有弹夹'

    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print('没有子弹了,放了空枪........')
laowang = Ren('老王')
danjia = Danjia(20)
i=0
while i < 5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+1
    print(danjia)
qiang = Qiang()
print(qiang)
laowang.anzidan(qiang,danjia)
print(qiang)


diren = Ren('敌人')
print(diren)


laowang,naqiang(qiang)

laowang.kaiqiang(diren)
print(diren)
print(danjia)


laowang.kaiqiang(diren)
print(diren)
print(danjia)
