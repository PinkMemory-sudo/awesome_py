import pandas as pd
import json
import glom

df = pd.read_json('nested_list.json')

print(df)
print(df.to_string())

with open('nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path=['students'])
print(df_nested_list)

# 可以用meta指定展开时同时附加的数据
with open('nested_mix.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)

# glom 模块允许我们使用 . 来访问内嵌对象的属性
from glom import glom

df = pd.read_json('nested_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
