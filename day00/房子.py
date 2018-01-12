"""
买房子:500万买一环。400买2环，300万３环，200万买4环，小于200万，睡大街
"""
money = int(input("请输入存款金额"))
if money>=500:
    print("可以买一环")
elif money>=400:
    print("可以买二环")
elif momey>=300:
    print("可以买三环")
elif momey>=200:
    print("可以买四环")
else:
    print("睡大街")
