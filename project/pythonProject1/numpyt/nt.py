import numpy as np

print(np.eye(4))

print("#" * 10)
a = np.array([1, 2, 3])
print(a)
print("#" * 10)
a = np.array([[1, 2], [3, 4]])
print(a)
a = [[1, 2], [3, 4]]
print(a)
print("#" * 10)
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
print("#" * 10)
a = np.array([1, 2, 3], dtype=complex)
print(a)
print("#" * 10)
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
print("#" * 10)
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(student)
print(a)
print("#" * 10)
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)
print("#" * 10)
print(a)
print(b)
print("#" * 10)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
print("#" * 10)
# 改变维度
a.shape = (3, 2)
print(a)
print("#" * 10)
b = a.reshape(2, 3)
print(b)
print("#" * 10)
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)
# 内存信息
print(y.flags)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, ])

#  数组元素为随机值，因为它们未初始化
x = np.empty([3, 2], dtype=int)
print(x)

# 元素用0填充
x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x)

# 元素用1填充
x = np.ones([2, 2], dtype=int)
print(x)

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)

print("#" * 10)
s = b"helloworld"
x = np.frombuffer(s, dtype='S1')
print(x)
print("#" * 10)
y = x.reshape((2, 5))
print(y)

# fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
r = range(15)
x = np.fromiter(r, dtype=float)
print(x)
x.shape = (3, 5)
print(x)

print("#" * 10)
x = np.arange(0, 30, 5, dtype=float)
print(x)
x.shape = (3, 2)
print(x)

# 等差数列创建数组
x = np.linspace(3, 33, 10, dtype=int, endpoint=True)
print(x.reshape((5, 2)))

# 等比数列创建数组
x = np.logspace(0, 9, 10, base=2, dtype=int, endpoint=False)
print(x)

print("#" * 10)
a = np.arange(10)
print(a)
s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print(s)
print(a[s])

# 切片
a = np.arange(10)
s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print(a[s])

a = np.arange(10)
b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

# 多维数组切片
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素

print("#" * 10)
x = np.array([[1, 2], [3, 4], [5, 6]])
# 获取数组中 (0,0)，(1,1) 和 (2,0) 位置处的元素
y = x[[0, 1, 2], [0, 1, 0]]
print(x)
print(y)

print("#" * 10)
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)
# 通过数组索引
rows = np.array([0, 0, 3, 3])
cols = np.array([0, 2, 0, 2])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)

# 通过布尔值索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
# 现在我们会打印出大于 5 的元素
print('大于 5 的元素是：')
print(x[x > 5])

# 花式索引  花式索引跟切片不一样，它总是将数据复制到新数组中
x = np.arange(9)
print(x)
# 一维数组读取指定下标对应的元素
print("-------读取下标对应的元素-------")
x2 = x[[0, 6]]  # 使用花式索引
print(x2)

print(x2[0])
print(x2[1])
print("#" * 10)
print(1.2 * 1.2 * 4)
print(1.2 * 0.8 * 4)
print(1 * 1 * 4)
print(1 * 0.8 * 4)
print(0.8 * 0.8 * 4)
print(0.8 * 1 * 4)
print(0.8 * 1.2 * 4)

x = np.arange(32).reshape((8, 4))
print(x)

# 产生笛卡尔集
x = np.arange(32).reshape((8, 4))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
print("#" * 10)

# 广播机制：当两个数组的形状不同时，维度相同且长度也相同,广播机制通过虚拟地复制较小的数组，使其与较大的数组具有相同的形状
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])

# 向量与标量
print(a+100)
print("#" * 10)
# 一维数组与二维数组
b = np.array([[0, 1, 2]
              ])
print(a + b)
print("#" * 10)
