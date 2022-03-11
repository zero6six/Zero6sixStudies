import random

print("掷硬币脚本")

chance = input("请输入你要投掷的次数 ")
up = 0
down = 0

display = input("请输入是否每次都要显示硬币结果(y/n) ")
print("")
if display == "y":
    display = True
elif display == "n":
    display = False
else:
    display = True
    print("输入不合法，自动开启显示")

try:
    chance = int(chance)
except ValueError:
    print("投掷次数必须为整数！")
else:
    if chance <1:
        print("投掷次数不能过大或过小！")
    else:
        for i in range(chance):
            Number = (random.randint(0, 1))
            if Number == 1:
                up += 1
                if display:
                    print("掷出的硬币为正面！")
            else:
                down += 1
                if display:
                    print("掷出的硬币为反面！")
        print("\n总共投掷", chance, "次\n正面", up, "次，反面", down, "次")
