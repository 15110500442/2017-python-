# 判断男女
sex = input("你是男的还是女的还是其他")
if sex == "男":
    height = input("你高吗")
    money = input("你富吗")
    shuai = input("你帅吗")
    if height == "高" and money == "富" and shuai == "帅" :
        print("高富帅")
    else :
        print("高富帅")
elif sex == "女":
    color = input("你白吗")
    money = input("你富吗")
    mei = input("你美吗")
    if color == '白' or money == '富' or mei == '美':
        print("白富美")
    else:
        print("丑比")
else:
    die = input('是死还是活')
    if not die == '活':
        print("死人妖")
    else:
        print("活人妖")
    
