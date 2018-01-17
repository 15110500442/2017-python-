#阿里面试
age = int(input("请输入你的年龄"))
print("学历初中以上的请输入2，学历以下的请输入1")
xueli = int(input("请输入你的学历"))
if age >=18 and xueli >= 2:
    print("欢迎加入阿里")
elif (age >= 18 and xueli < 2) or (age < 18 and xueli >= 2):
    print("参加第二次面试")
else:
    print("sorry，你没有通过本公司的面试")
