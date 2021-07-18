print("英语月份小工具")

Months = ("January","February","Marth","April","May","June",
"July","August","September","October","Novenmber","December")

Input = input("请输入待转换月份的数字")

try:                      # 错误处理，由星域世界内测群 Tom 教授
    int(Input)
except ValueError:
    print("输入不合法")
else:
    if int(Input)<=12 and int(Input)>=1:
        Number = int(Input) - 1
        Output = Months[Number]
        print("转换后月份为",Output)
    else:
        print("输入不合法")