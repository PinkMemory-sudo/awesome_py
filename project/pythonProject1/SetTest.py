# 创建空集合只能用set()
a = set("asdfgwefsadaserv")
print(a)
b = set("asdd")
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


def get_empty_set():
    print("empty set")
    return set()


def get_set(param):
    print("set")
    return set(param)
