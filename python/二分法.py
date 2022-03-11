'''
二分法求方程近似解
number 为精确度
[a,b]为方程存在零点的区间
func 函数内部即为需要求的方程
待使用更精确的计算方法优化 
'''

number = 0.1             
a=0
b=2

def func(number):
    '''对函数进行计算'''
    number=3.14*number-2
    return number

def func2(number):
    '''求绝对值'''
    if number<0:
        number =-number
    else:
        pass
    return number

while True:
    c=(a+b)/2
    if func(a)*func(c)<0:
        b=c
    elif func(c)==0:
        a=c
        break
    else:
        a=c
    if func2(a-b)<number:
        break
    else:
        continue

print(a)