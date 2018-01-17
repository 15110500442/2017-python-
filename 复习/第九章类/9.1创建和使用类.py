
class Dog():
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age
    def sit(self):
        '''模拟小狗被命令是蹲下'''
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        '''模拟小狗被命令打滚'''
        print(self.name.title() + "rolled over!")
dog = Dog('牧羊犬','15')
dog.sit()
dog.roll_over()

print('------------------------------------------------')

my_dog = Dog('金毛','5')
your_dog = Dog('阿拉斯加','5')
print("My dog's name is " + my_dog.name.title() + ".")
print('My dog is ' + str(my_dog.age) + 'years old.')
my_dog.sit()
print("\n Your dog's name is  " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + "years old.")
your_dog.sit()

