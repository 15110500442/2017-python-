class Kao_digua:
    def __init__(self):
        self.sheng_shu_du = 0
        self.sheng_shu_du_str = '生'
        self.peiliao = []
    def kao(self,times):
        self.sheng_shu_du += times
        if self.sheng_shu_du > 8:
            self.sheng_shu_du_str = '烤胡了'
        elif self.sheng_shu_du > 5:
            self.sheng_shu_du_str = '熟了'
        elif self.sheng_shu_du > 3:
            self.sheng_shu_du_str = '半生不熟'
        else:
            self.sheng_shu_du_str = '生的'
   
   
   
    def __str__(self):
        msg = self.sheng_shu_du_str + '地瓜'
        if len(self.peiliao) > 0:
            msg = msg +msg+'('
            for temp in self.peiliao:
                msg = msg + temp + ','
            msg = msg.strip(',')
            msg = msg + ')'
        return msg
    def tianjia(self,peiliao):
        self.peiliao.append(peiliao)

potato = Kao_digua()
print('--------有一个地瓜，还没有进行烤-----------')
print(potato.sheng_shu_du)
print(potato.sheng_shu_du_str)
print(potato.peiliao)  
print('---------接下来要进行烤地瓜----------------')
print('---------地瓜已经烤了4分钟-----------------')
potato.kao(4)
print(potato)
print('---------地瓜又烤了3分钟-------------------')
potato.kao(3)
print(potato)
print('---------要加番茄酱了----------------------')
potato.tianjia('番茄酱')
print(potato)
print('----------地瓜又烤了5分钟------------------')
potato.kao(5)
print(potato)
print('----------地瓜接下来妖添加芥末了-----------')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
