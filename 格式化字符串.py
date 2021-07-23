template = "{:0>6s}\t{:s}\t¥{:.2f}"
number1 = 0

while True:
    inputText = input("请输入商品信息（商品名 单价），按 0 退出：")
    if inputText == "0":
        break
    else:   
        number1 +=1
        list1 = inputText.split()          # 将输入字符串拆分成名称和金额的列表
             
        number2 = str(number1)             # 将序号转换为字符串型
        text = list1[0]                    # 将列表中的名称转换为字符串型
        money = float(list1[1])            # 将列表中的金额转换为浮点型
        print(template.format(number2,text,money))