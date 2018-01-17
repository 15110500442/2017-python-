age = int(input('请输入你的年龄'))
if age < 2:
    print('属于婴儿阶段')
elif age <= 4 and age >= 2:
    print('可以进行学走步了')
elif age <= 13 and age > 4:
    print('儿童哦，可以参加六一儿童节')
elif age <= 20 and age > 13:
    print('青少年')
elif age <= 65 and age > 20:
    print('成年人')    
else:
    print('老年人')
