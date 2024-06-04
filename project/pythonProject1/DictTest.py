a = {"name": "Feng.h", "age": 18, "companies": "LX"}
# 获得所有key，按插入次序排列
print(list(a))
# 是否包含某个key
print("name" in a)
del a["companies"]
print(a)
# dict+键值对序列构造函数创建字典
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# dict+关键字创建字典
a = dict(name="tom", age=18)
print(a)
# 推导式创建字典
a = {x: x ** 2 for x in (2, 4, 6)}
print(a)
# 用items()遍历，同时获得键和值
for k, v in a.items():
    print(k, v)
