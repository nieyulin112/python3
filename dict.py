# 在其他语言中也称为map，使用键-值（key-value）存储
dict = {'math': 100, 'english': 150}
print(dict['math'])

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# 需要牢记的第一条就是dict的key必须是不可变对象。