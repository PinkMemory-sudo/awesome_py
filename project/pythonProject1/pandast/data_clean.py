import pandas as pd
from pandas import DataFrame

# 数据清洗，将数据缺失、数据格式错误、错误数据或重复数据过滤掉
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
# dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# 清洗空值
df = pd.read_csv('property-data.csv')
print(df)
print(df['NUM_BEDROOMS'])
# 可以通过 isnull() 判断各个单元格是否为空
print(df['NUM_BEDROOMS'].isnull())

#  Pandas 把 n/a 和 NA 当作空数据,我们可以指定空数据类型
missing_values = ["n/a", "na", "--"]
df = pd.read_csv('property-data.csv', na_values=missing_values)

print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())
print(df)
df.dropna(inplace=True)
print(df)

# 移除指定列有空值的
df = pd.read_csv('property-data.csv')

df.dropna(subset=['ST_NUM'], inplace=True)

print(df.to_string())

# fillna() 方法来替换一些空字段
df = pd.read_csv('property-data.csv')
df.fillna(11223, inplace=True)
print(df.to_string())

df = pd.read_csv('property-data.csv')
df['PID'].fillna(12345, inplace=True)
print(df.to_string())

# 清洗格式错误数据
data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

# 清洗错误数据
person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 40, 12345]  # 12345 年龄数据是错误的
}
df = pd.DataFrame(person)
df.loc[2, 'age'] = 30  # 修改数据
print(df.to_string())

# 清洗重复数据
person = {
    "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
    "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)
print(df.duplicated())
