#阿里面试
age = int(input("请输入你的年龄"))
xueli = int(input("请输入你的学历"))
xueli = 2
if age > 18:
    if xueli >= 2:
        print("录取")
    elif xueli < 2:
        print("第二次面试")
elif age < 18:
    if xueli >= 2:
        print("第二轮面试")
    elif xueli < 2:
        print("滚肚子")
else:
    print()
   
