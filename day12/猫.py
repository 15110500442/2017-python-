class Cat(object):
    def __init__(self,name,color='白'):
        self.name = name
        self.color = color
        self._eyes = '三只眼'#这是私有属性，别人是不会读取和修改的
    def run(self):
        print('抓老鼠')
    def _kai(self):#这是一个私有的方法，别人是不可以读取的和修改的
        print('开天眼')
    def getEyes(self):#这是在一个获取私有方法的一个函数（程序员的约定）
        return self._eyes
    def` 


