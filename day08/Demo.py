print("欢迎进入阿里云面试系统！！")
age = int(input("请输入您的年龄"))
student = str(input ("请输入您的学历"))
if age >18 and student == 初中:
    print("您符合我们的要求，恭喜您")
    return true
elif age >18 and student == 小学:
    print("您有一项不符合我们的要求，请进入第二轮面试")
    return false
elif age <18 and student == 初中:
    print("您有一项不符合我们的要求，请进入第二轮面试")
    return false
elif age <18 and student == 小学:
    print("您两项都不符合我们的要求，很抱歉！")
    return fase
  
