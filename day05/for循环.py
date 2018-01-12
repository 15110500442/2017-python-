for nihao in range(1,10):
    print(nihao)
    for col in range(1,10):
        print("%d*%d=%d"%(nihao,col,nihao * col),end="\t")
    col += 1
    print("")
