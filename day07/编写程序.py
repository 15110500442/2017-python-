lerrer = 0
number = 0
space = 0
sumbol = 0


name = '人生苦短，我用python，life is need short'
s = name ()
for char in s:
    if 'a'<= char <= 'z' or 'A' <= char <='Z':
        letter+=1
    elif 0 <= char <= 9:
        number+=1
    elif char == ['','']:
        space+=1
    else:
        symbol+=1
print'字母数量，数字数量，空格数量，其字符的数量分别是:'
print letter,nukber,space symnol
