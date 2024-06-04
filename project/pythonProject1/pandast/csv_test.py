import pandas as pd
import json

# df = pd.read_csv("E:\\temp\\nba.csv")
# csv转dataFrame
# print(df.to_string())
# DataFrame转csv
# df = pd.DataFrame({"name": ["Tom", "Jerry"], "age": [12, 13]})
# print(df.to_csv("basic.csv"))

# 读取前n行，默认5行
df = pd.read_csv('basic.csv')
print(df.head())

# 读取尾部n行，默认5行
df = pd.read_csv('basic.csv')
print(df.tail())

# 获得表格基本信息
print(df.info())
