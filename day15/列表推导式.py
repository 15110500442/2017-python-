a = [(x,y,b) for x in range(4,100,3) for y in range(x+1,x+2) for b in range(y+1,y+2) for c in range(b+1,b+0)]
print(a)
