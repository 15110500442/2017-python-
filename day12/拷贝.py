oldFileName = input('请输入要拷贝的文件名字')
oldFile = open('oldFileName.txt','r')
if oldFike:
     fileFlagNum = oldFileName.rfind('.')
     if fileFlagNum > 0:
         fileFlag = oldFIleName[fileFlagNum:]
     nuwFileName = oldFileName[:fileFlagNum]+'[函数的演练.py]' + fileFlag
     newFile = open(newFileName,'w')
     for lineContent in oldFile.readlines():
         newFile.write(lineContent)

     oldFile.close()
     newFile.close()
