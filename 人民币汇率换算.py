# 人民币-CNY 美元-USD 英镑-GBP 欧元-EUR 日元-JPY

def transform(CNY):
    USD = round(CNY*0.1546,2)
    print(number,"CNY=",USD,"USD")
    GBP = round(CNY*0.1126,2)
    print(number,"CNY=",GBP,"GBP")
    EUR = round(CNY*0.1284,2)
    print(number,"CNY=",EUR,"EUR")
    JPY = round(CNY*16.2935,2)
    print(number,"CNY=",JPY,"JPY")

print("本工具可将输入的人民币金额转换为美元，英镑，欧元和日元金额")
number = float(input("请输入人民币金额(CNY) "))
transform(number)