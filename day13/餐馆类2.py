#餐馆类
class Restaurant(object):
    def __init__(self):
       self.restaurant_name = 'jjjjj'
       self.cuisiine_type = 'llll'
   def describe_restaurant(self):
       print(self.restaurant_name)
       print(self.cuisiine_type)
   def open_restaurant(self):
       print('正在营业')
restaurant = Restaurant()
print(restaurant.restaurant_name,restaurant.cuisiine_type)
restaurant.describe_restaurant()
restaurabt.open_restaurant()
