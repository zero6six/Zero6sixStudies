# 对桌面上的 en_us.lang 进行翻译

import myModule

file2 = open(r"C:\users\zero6six\desktop\zh_cn.lang", "w+",encoding="utf8")

with open(r"C:\users\zero6six\desktop\en_us.lang") as file:
    text = file.readlines()
for i in range(len(text)):
    if text[i] == "\n" or text[i].count("#")>0:
        file2.write(text[i])
    else:
        list1 = text[i][:len(text[i])-1].split("=") 
        zhText = myModule.translate(list1[1])
        outputText = list1[0] + "=" + zhText
        print(outputText)
        file2.write(outputText + "\n")

file2.close()
