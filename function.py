# abs函数
print(abs(-100))
# max函数
print(max(1,2,3,-5))
# int函数
print(int('123'))
# str函数的应用
print(str(123))
# float函数
print(float('12'))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))

def nop():
    pass
