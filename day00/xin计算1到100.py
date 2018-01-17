sum_1 = 0
sum_2 = 0
i = 0
while i <= 100:
    if i%2 == 0:
        sum_2 = sum_2 + i
   else:
       sum_1 = sum_1 + i
    i += 1
print("和%d"%sum_1,sum_2)
