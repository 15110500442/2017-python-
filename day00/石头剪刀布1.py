import random
i = 0
while i < 50:
    playerStr = int(input("请出拳 石头(1)/剪刀(2)/布(3):"))
    player = int(playerStr)
    mac = random.randint(1,3)
    if (player == 1 and mac == 2) or (player == 2 and mac == 3) or (player == 3 and mac == 1):
        print("呵呵，运气真好，赢了。")
    elif player == mac:
        print("平局，要不要再来一局")
    else:
        print('我也赢了，刚才得瑟毛线')
    i += 1
