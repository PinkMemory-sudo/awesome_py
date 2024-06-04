a = [1]
a.extend([1, 2, 3])
print(a)
a.append(2)
print(a)
a.insert(0, 4)
print(a)
# 找不到时报错
a.remove(1)
print(a)
print(a.pop())
# 找不到时报错
a.index(1, 0, len(a))
print(a.count(1))
print(len(a))
# 直接修改原列表的
a.sort()
print(a)
a.reverse()
print(a)
a.clear()
print(a)

# 列表推导式
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares = list(map(lambda y: y ** 2, range(10)))
# map并不是字典，而是一个函数，一个函数和一个可迭代对象。它将函数应用到可迭代对象的每个元素上，返回一个map对象(可迭代)
mm = map(lambda y: y ** 2, range(10))
for k in mm:
    print(k)
print(squares)
# [expression for item in iterable],将右边的每个元素放到左边去求值
squares = [x ** 2 for x in range(10)]
print(squares)

squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares)

# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 嵌套的推导式
squares = [[row[i] for row in matrix] for i in range(4)]
print(10 * "=")
print(squares)
print(10 * "=")
# zip函数更方便
zp = zip(*matrix)
zp_list = list(zp)
print(zp_list)
print(10 * "=")
# del按照下标删除元素，也可用于从列表中移除切片或清空整个列表
del zp_list[2:]
print(zp_list)
print(10 * "=")
a = 1, 1
print(len(a))
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = list(zip(a, b))
print(c)


def get_t():
    print("xi")
