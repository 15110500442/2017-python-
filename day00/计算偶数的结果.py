result1 = 0
result2 = 0
i = 0 
while i <= 100:
    if i%2 == 1:
        print(i)
        result1 += i
    else:
        result2 += i

   
print("和%d"%result1,result2)
