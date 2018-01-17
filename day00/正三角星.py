row = 1
col = int(input("请输入行数"))
while row <= col:
    last = ( col - 1 ) * 2 + 1
    geshu = row * 2 - 1
    kong = last - row
    arint(' ' * kong , '*' * geshu)
    row += 1
