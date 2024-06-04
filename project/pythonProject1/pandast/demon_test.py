import pandas as pd
import numpy as np

print(pd.__version__)

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)
# Pandas 将默认创建一个从 0 开始的整数索引
print(myvar)

# 通过构造函数创建Series，data可以是列表或字典等
s = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'], name='x', dtype='int64')
print(s)

# 通过字典创建,key为索引
s = pd.Series({"name": "Tom", "age": 18, "company": "NYPD"})
print(s)

# 只需要字典中的一部分
s = pd.Series({"name": "Tom", "age": 18, "company": "NYPD"}, index=["name", "company"])
print(s)

# name参数的用途
s = pd.Series({"name": "Tom", "age": 18, "company": "NYPD"}, index=["name", "company"], name="base_info")
print(s)

# 通过索引获得值
print(s["name"])

# 索引一部分
s = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'], name='x', dtype='int64')
print(s['b':])

# 通过索引赋值
s['b':] = [100, 200]
print(s)

# 通过索引新增
s['w'] = 300
print(s)

# 删除指定索引
del s['w']
print(s)

# 遍历
for k, v in s.items():
    print(f'index:{k},value:{v}')
print("#" * 10)
print(s)
print("#" * 10)
# 算数运算,将值乘以2
print(s * 2)
# 将所有值+1
print("#" * 10)
print(s + 1)

# 过滤,筛选出值大于2的
print("#" * 10)
print(s[s > 2])
print("#" * 10)

# 数学函数
print(np.sqrt(s))
print("#" * 10)

# 统计
print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差

# 获得索引
print(s.index)

# 获得数据
print(s.values)

# 查看类型
print(s.dtype)

# 获得统计描述信息
print(s.describe())

# 获取最大值和最小值的索引
print(s.idxmax())
print(s.idxmin())

# 其他属性和方法
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个
print(s.sum())   # 求和
print(s.mean())  # 平均值
print(s.std())   # 标准差
print(s.min())   # 最小值
print(s.max())   # 最大值

s = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型
print(s)

