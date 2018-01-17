yao_qing = ["李大","张三","李四","王五"]
for i in yao_qing:
   print("邀请%s一起共进晚餐"%i)
print("由于王五在工作上的情况，无法赴约")
yao_qing2 = "赵六"
print("最后赴约的人是%s"%yao_qing2)
yao_qing3 = ['李大','张三','李四','赵六'] 
for i in yao_qing3:
    print("邀请%s一起来共进晚餐"%i)
print("由于想换一个大的餐厅，准备在邀请几个")
print("邀请小明,钱八,孙九来共进晚餐")
len(yao_qing3)
print('还剩%s'%(len(yao_qing3)))
yao_qing3.insert(0,'小明')
yao_qing3.insert(2,'钱八') #  yao_qing3.insert(
yao_qing3.append('孙九')
for i in yao_qing3:
    print("邀请%s一起来共进晚餐"%i)
print("由于餐厅人满，新的餐桌无法送达。只能邀请2位嘉宾")
yao_qing3.pop()
print("不好意思啊小明，钱丢了，下次请你吃大餐")
yao_qing3.pop()
print("不好意思啊钱八，钱丢了，下次请你吃大餐")
yao_qing3.pop()
print("不好意思啊孙九，钱丢了，下次请你吃大餐")
yao_qing3.pop()
print("不好意思啊李大，钱丢了，下次请你吃大餐")
yao_qing3.pop()
print("不好意思啊李四，钱丢了，下次请你吃大餐")
print("赵六，过来吃饭吧")
print("张三，过来吃饭吧")
del yao_qing3[0:2]
print(yao_qing3)
