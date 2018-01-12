name = str(input("请输入你的名字"))
height = float(input("请输入你的身高"))
weight = float(input("请输入你的体重"))
BMI = weight / (height**2)
if BMI < 18.5:
    print("%s的BMI为%s属于过轻"%(name,BMI))
elif BMI >= 18.5 and BMI <= 25:
    print("%s的BMI为%s属于正常"%(name,BMI))
elif BMI > 25 and BMI<= 28:
    print("%s的BMI为%s属于过重"%(name,BMI))
elif BMI > 28 and BMI<= 32:
    print("%s的BMI为%s属于肥胖"%(name,BMI))
elif BMI > 32:
    print("%s的BMI为%s属于严重肥胖"%(name,BMI))
else:
    print()
