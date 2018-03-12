# Python内建了map()和reduce()函数。
# 我们先看map。map()函数接收两个参数，
# 一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。

def mul(x):
    return pow(x, 2)
r = list(map(mul, [1,2,3,4,5,6]))
print(r)

s = list(map(str, [1,2,3,4,5]))
print(s)
