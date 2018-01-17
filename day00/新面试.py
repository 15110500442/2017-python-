#阿里面试
print("欢迎来到阿里面试系统")
age = int(input("请输入你的年龄："))
education = int(input("请输入您的学历：(初中以上请输入1,初中以下请输入2)"))
if age >=18 and education == 1:
    print("欢迎加入阿里")
elif age >= 18 and education == 2 or age < 18 and education == 1:
    print("您进入第二轮面试")
elif age < 18 and education == 2:
    print("很抱歉，你不符合我们公司的要求")
