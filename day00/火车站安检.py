has_ticket = int(input("请输入是否有车票"))
if has_ticket==True:
    print("可以进入安检程序")
    hsnife_length = float(input("请输入刀的长度"))
    if hsnife_length >= 20:
        print("不允许上车")
    else:
        print("可以上车")
else:
    print("请去买票")
