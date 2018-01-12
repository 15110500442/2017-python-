class Aaimal(object):
    def zu(self):
        print('祖宗')
class Ma(Aaimal):
    def __init__(self):
        zi_G = '有'
    def fly(self):
        print('飞')
    def heihei(self):
        print('我会嘿嘿')
    def zu(self):
        print('我是新祖宗')
class Lv(Aaimal):
    def __init__(self):
        BZ = '有'
    def swin(self):
        print('游')
    def heihei(self):
        print('我会赫赫')
class LZ(Ma,Lv):
    def haha(self):
        print('我会哈哈')
    def heihei(self):
        print('我呵呵')
    def zu(self):
    print('我是最新的祖宗')
骡子 = LZ()
骡子.swin()
骡子.fly()
骡子.haha()
骡子.heihei()
骡子.zu()
