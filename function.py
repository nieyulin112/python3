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

# pow 默认参数
def power(x = 10, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 2))
print(power(5, 1))
print(power())

# 函数的理解, 参数, 参数类型，函数返回值
# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
