import pandas as pd

# 使用二维数组创建
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])
print(df)
print("#" * 10)

# 使用字典创建，指定每一列的值,长度必须一致
data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)
print(df)
print("#" * 10)

# 使用字典的key-value创建,key可以不一样，缺少的值用NaN补全
d = pd.DataFrame([{"name": "tom", "age": 18, 'gender': "female"},
                  {"name": "jerry", "age": 23, "company": "Navd"},
                  {"name": "moni", "age": 18, 'gender': "female"}
                  ])
print(d)
print("#" * 10)

# 从 Series 创建 DataFrame
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
print(df)
print("#" * 10)

# 根据索引获得某一(多)行,(一行就得到一个Series，多行就是DataFrame  )
print(d.loc[[1, 2]])
print("#" * 10)

# 访问某一列
# d.name 是属性访问方式，可能会与 DataFrame 的方法或属性名冲突
print(d.name)
# DataFrame 列的标准方法，适用于任何列名,Pandas 不允许通过添加新的属性来创建新的列 推荐使用d["name"]
print(d["name"])
print("40#" * 10)

# 访问某个元素
print(d.name[1])
print("44#" * 10)
# 指定索引
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc[["day2"]])
print("#" * 10)

# DataFrame 的属性和方法
print(df.shape)  # 形状
print(df.columns)  # 列名
print(df.index)  # 索引
print(df.head())  # 前几行数据，默认是前 5 行
print(df.tail())  # 后几行数据，默认是后 5 行
print(df.info())  # 数据信息
print(df.describe())  # 描述统计信息
print(df.mean())  # 求平均值
print(df.sum())  # 求和
print("#" * 10)

# 添加修改列的值
print(df)
df.duration = [1, 2, 3]
df["city"] = ["shanghai", "beijing", "Chicago"]
print(df)

# 添加新行，列数要对上
df.loc["day4"] = [1, 2, "wuhan"]
print(df)

# drop 方法默认不改变原 DataFrame，而是返回一个新的 DataFrame,为了修改原 DataFrame，需要 inplace=True,axis=1表示对列进行操作
# 删除列
df.drop("city", axis=1, inplace=True)
print(df)
# 删除行,会生成新的dataFrame,旧的不变
df.drop("day4", inplace=True)
print(df)

print("统计摘要")
print(df.describe())

# 使用聚合函数如 .sum()、.mean()、.max() 等。
print(df["calories"].sum)
print(df.mean())

# 合并

import pandas as pd

# 创建两个示例 DataFrame
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
})

# 垂直合并
result = pd.concat([df1, df2])
print("Vertical Concatenation:\n", result)

# 水平合并
result = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", result)


# merge 类似于 SQL 中的 JOIN 操作，匹配不上的不join
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K4'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

# 合并 DataFrame
result = pd.merge(left, right, on='key')
print("\nMerge Result:\n", result)

# join 方法用于基于索引合并两个，匹配不上的为空
left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

right = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])

# 使用 join 合并 DataFrame
result = left.join(right, how='outer')
print("\nJoin Result:\n", result)

# 分割
df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

# 使用 iloc 按位置分割 DataFrame
part1 = df.iloc[:2]
part2 = df.iloc[2:]

print("\nFirst Part using iloc:\n", part1)
print("\nSecond Part using iloc:\n", part2)

# 使用 loc 按标签分割 DataFrame
part1 = df.loc[:1]
part2 = df.loc[2:]

print("\nFirst Part using loc:\n", part1)
print("\nSecond Part using loc:\n", part2)

# group by 按照某列的值进行分组
df = pd.DataFrame({
    'key': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'data': range(8)
})

# 按 'key' 列分组
grouped = df.groupby('key')

# 查看每个组的内容
for name, group in grouped:
    print(f"\nGroup name: {name}")
    print(group)
