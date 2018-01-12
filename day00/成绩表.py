math = int(input("请输入你的数学成绩单"))
if math >= 61:
    print("通过")
    chinese = int(input("请输入你的语文成绩单"))
    if chinese >= 60:
        print("通过")
    else:
        print("补考")
else:
    print("不通过")
