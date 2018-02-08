# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 基本的两个方法 add() remove()
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(5)
print(s)
s.remove(3)
print(s)

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 但是，因为无法判断两个可变对象是否相等，
# 也就无法保证也就无法保证set内部“不会有重复元素”。

a = '123'
s = a.replace('1', '2')
print(s)
print(a)
