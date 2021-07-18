import random

MaxNumber = 100                                                         # 对 MaxNumber 进行赋值
Number = (random.randint(0,MaxNumber))                                  # 对 Number 赋一个大于 0，小于 MaxNumber 的值
Chance = 5                                                              # 对 Chance 进行赋值

print("竞猜")
print("猜一个在0~" + str(MaxNumber) + "之间的数")
print("您有" + str(Chance) + "次机会")

while Chance>=0:                                                        # 当 Chance 大于 0 时进入循环
    if Chance>0:                                                        # 当 Chance 大于 0 时可进行竞猜
        Input = int(input("请输入你猜的数字"))
    Chance -=1                                                          # 在输出剩余 Chance 时先扣除 1
    if Chance == 0:                                                     # 若 Chance 为 0，竞猜结束
        print("对不起，您没有猜中，本次竞猜的数字为" + str(Number))
        break
    if Input>Number:
        print("您输入的数字大了，您还有" + str(Chance) + "次机会")
    if Input<Number:
        print("您输入的数字小了，您还有" + str(Chance) + "次机会")
    if Input==Number:
        print("恭喜，您猜中了")
        break