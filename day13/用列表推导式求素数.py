a = [x for x in range(2,100) if not [y for y in range(2,x) if x%y ==0]]
print(a)

