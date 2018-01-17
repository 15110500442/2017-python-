money = 1
distance = int(input("请输入距离"))
day = 1
while day <= 20:
    count = 1
    while count <= 2:
        if money <= 100:
            if distance <= 6:
                money += 3
            elif distance > 6 and distance <= 12:
                money += 4
            elif distance > 12 and distance <= 22:
                money += 5 
            elif distance > 22 and distance <= 32:
                money += 6
            elif distance > 32:
                if (distance - 32)%20 == 0:
                    money +=(6+(distance - 32)/20)
                else:
                    money +=(6+(distance - 32)/20+1)
        if money > 100 and money <= 150:
            if distance <= 6:
                money += 3*0.8
            elif distance > 6 and distance <= 12:
                money += 4*0.8
            elif distance >12 and distance <= 22:
                money += 5*0.8
            elif distance >22 and distance <= 32:
                money += 6*0.8
            elif distance >32:
                if (distance - 32)%20 == 0:
                    money +=(6+(distance - 32)/20)*0.8
                else:
                    money +=(6+(distance - 32)/20+1)*0.8
        if money > 150 and money <= 400:
            if distance <= 6:
                money += 3*0.5
            elif distance > 6 and distance <= 12:
                money += 4*0.5
            elif distance > 12 and distance <= 22:
                money += 5*0.5
            elif distance > 22 and distance <= 32:
                money += 6*0.5
            elif distance > 32:
                if (distance - 32)%20 == 0:
                    money +=(6+(distance - 32)/20)*0.5
                else:
                    money +=(6+(distance - 32)/20+1)*0.5
        if money > 400:
            if distance <= 6:
                money += 3
            elif distance > 6 and distance <= 12:
                money += 4
            elif distance > 12 and distance <= 22:
                money += 5
            elif distance > 22 and distance <= 32:
                money += 6 
            elif distance > 32:
                if (distance - 32)%20 == 0:
                    money += (6+(distance - 32)/20)
                else:
                    money += (6+(distance - 32)/20+1)
        count += 1
    day += 1
print("小明一共花费了%.2f元"%money)
               
         
