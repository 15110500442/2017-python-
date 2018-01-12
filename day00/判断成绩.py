#判断成绩
python_score = int(input("请输入你的pyhton_score成绩"))
c_score = int(input("请输入你的c_score成绩"))
if python_score >= 60 and c_score < 60 or python_score < 60 and c_score >= 60:
    print("合格")
else:
    print("不合格")


