count = 0
bang_zhu = 0
while count<=5 and bang_zhu !=1:
    print('目前在第%d杀'%count)
    bang_zhu = int(input("班主任来了没"))
    if bang_zhu == 1:
        print('当在第%d杀的时候，班主任来了'%count)
        bang_zhu = 0
        continue
    count += 1
if count>=5:
    print('游戏胜利了')
else:
    print('游戏结束')
