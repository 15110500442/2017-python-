for count in range (2,10):
    num = int(input("请输入你本次抓娃娃需要多少秒(1-60秒)"))
    if num > 30:
        print("时间到了，机器自动抓给你了")
        continue
    else:
        print("你本次用了%d秒抓了一下"%num)
