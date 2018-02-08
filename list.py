# list是有序数组
classMates = ['1', '2', '3']
print(len(classMates))
# 插入元素
classMates.insert(1, 'jack')
print(classMates)
# 要删除list末尾的元素用pop()方法
classMates.pop()
print(classMates)

# 要删除指定的
classMates.pop(0)
print(classMates)

# tuple:另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tclass = (1,2,3)
print(tclass)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
arr = [1,2,3,4,5,6,7,8,9];
for x in arr:
    sum = sum + x
print(sum)

#list
print(list(range(10)))

sum = 0
for i in range(101):
    sum = sum + i
print(sum)


# dict和set
