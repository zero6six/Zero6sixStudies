import random

print("掷硬币脚本")
string = (input("请输入你要投掷的次数 "))
try:
    maxChance = int(string)
except ValueError:
    print("输入不合法")
else:
    for i in range(maxChance):
        Number = (random.randint(0,1))
        if Number == 0:
            print("掷出的硬币为反面！")
        else:
            print("掷出的硬币为正面！")
