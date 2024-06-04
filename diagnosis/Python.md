# Python

数据结构

数据类型

数组

字典

模块

标准模块

函数



?

* 解包
* as
* 具名常量



## 字符串

```shell
python -c command [arg] ...

# Python 模块也可以当作脚本使用。
python -m module [arg] ...

# 在交互模式下运行脚本文件，只要在脚本名称参数前，加上选项 -i 就可以了

# 读取命令行参数 sys 模块的 argv 变量，解释器不处理 -c command 或 -m module 之后的选项，而是直接留在 sys.argv 中由命令或模块来处理。
# 交互模式下，上次输出的表达式会赋给变量 _
```

```
除法运算 (/) 总是返回浮点数
得到一个整数结果你可以使用 // 运算符
用 ** 运算符计算乘方
Python 还支持其他数字类型，例如 Decimal 或 Fraction。Python 还内置支持 复数，后缀 j 或 J 用于表示虚数（例如 3+5j ）
如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可： print(r'\naha')
r'C:\this\will\not\work\'
字符串字面值可以包含多行。 一种实现方式是使用三重引号："""...""" 或 '''...'''
字符串可以用 + 合并（粘到一起），也可以用 * 重复：
相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并,只能用于两个字面值   'Py' 'thon'='Python'
字符串支持 索引 （下标访问），第一个字符的索引是 0,结果包含切片开始，但不包含切片结束,索引越界会报错,切片会自动处理越界索引
Python 字符串不能修改,为字符串中某个索引位置赋值会报错
内置函数 len() 返回字符串的长度

```

参见



- [文本序列类型 --- str](https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq)

  字符串是 *序列类型* ，支持序列类型的各种操作。

- [字符串的方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods)

  字符串支持很多变形与查找方法。

- [f 字符串](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings)

  内嵌表达式的字符串字面值。

- [格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#formatstrings)

  使用 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 格式化字符串。

- [printf 风格的字符串格式化](https://docs.python.org/zh-cn/3/library/stdtypes.html#old-string-formatting)

  这里详述了用 `%` 运算符格式化字符串的操作。



## 列表

列表 可以包含不同类型的元素，但一般情况下，各个元素的类型相同

列表也支持索引和切片，可变类型，`letters[2:5] = ['C', 'D', 'E']` 清空`letters[2:5] = []`

普通复制得到列表的引用，切片得到新列表

支持合并操作 （+）

`len(letters)`也支持列表

列表中的元素可以是个列表

```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
```



```python
list.append()
```





多重赋值,等号右边的所有表达式的值，都是在这一语句对任何变量赋新值之前求出来的

关键字参数 *end* 可以取消输出后面的换行, 或用另一个字符串结尾





## 流程控制

```python
if xxx :
    xxx
elif xxx:
	xxx
else:
    xxx
```



Python 的 `for` 语句不迭代算术递增数值,或是给予用户定义迭代步骤和结束条件的能力,而是在列表或字符串等任意序列的元素上迭代，按它们在序列中出现的顺序

很难正确地在迭代多项集的同时修改多项集的内容。更简单的方法是迭代多项集的副本或者创建新的多项集：

遍历列表

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

遍历字典

```python
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
```

[循环的技巧](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-loopidioms)

同时循环两个或多个序列时，用 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip)

在序列中循环时，用 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 函数可以同时取出位置索引和对应的值：

为了逆向对序列进行循环，可以求出欲循环的正向序列，然后调用 [`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed) 函数：

使用 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 去除序列中的重复元素。使用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 加 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 则按排序后的顺序，循环遍历序列中的唯一元素：



内置函数 range() 用于生成等差数列，可以指定范围和步长

range() 返回的对象在很多方面和列表的行为一样，但其实它和列表不一样，该对象只有在被迭代时才一个一个地返回所期望的列表项，并没有真正生成过一个含有全部项的列表，从而节省了空间



`for` 或 `while` 循环可以包括 `else` 子句。

```
在 for 循环中，else 子句会在循环成功结束最后一次迭代之后执行。

在 while 循环中，它会在循环条件变为假值后执行。
```



pass 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句



### 循环



* 当对字典执行循环时，可以使用 items() 方法同时提取键及其对应的值。
* 在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：
* 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：
*  逆向对序列进行循环，调用 reversed() 函数
*  sorted() 函数，在不改动原序列的基础上，返回一个重新的序列，按指定顺序循环序列
* 使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的唯一元素



* 比较运算符 in 和 not in 用于执行确定一个值是否存在（或不存在）于某个容器中的成员检测。
* 运算符 is 和 is not 用于比较两个对象是否是同一个对象
* a < b == c
* 在表达式内部赋值必须显式使用 海象运算符 :=
* 序列对象可以与相同序列类型的其他对象比较





## 模块

模块是包含 Python 定义和语句的文件

在模块内部，通过全局变量 __name__ 可以获取模块名（即字符串）

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 import 语句 第一次 遇到模块名时执行

```python
import ListTest
from SetTest import get_empty_set
import DictTest as fib
from DictTest import *
from SetTest import get_set as fibonacci
```

导入模块时会执行模块中的代码

```python
# 用于确定当前脚本是否作为主程序运行，确保某些代码仅在该脚本被直接运行时执行，而在该脚本被其他模块导入时不执行
if __name__ == "__main__":
    main()
```

```bash
# 当作脚本执行时，会把 __name__ 赋值为 "__main__"
python xxx.py
```

### 模块搜索路径

可以通过检查 sys.path 列表来查看 Python 当前的模块搜索路径





在 Python 命令中使用 -O 或 -OO 开关，可以减小编译模块的大小。-O 去除断言语句，-OO 去除断言语句和 __doc__ 字符串



内置函数 dir() 用于查找模块定义的名称(方法，变量等)

## 包



## 错误与异常

错误指的是语法错误

异常指的是写的语法没有错误，执行时才检查出来的错误

异常的处理

```python
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

**异常参数** 

内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args。





**触发异常**

raise 唯一的参数就是要触发的异常

**异常链**













## 















































































## match 

match 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较,与switch不一样的是，它更像是模式匹配，只有第一个匹配的模式会被执行，并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。



```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
       # 注意最后一个代码块：“变量名” _ 被作为 通配符 并必定会匹配成功。如果没有 case 匹配成功，则不会执行任何分支。
    
    match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
        
    
    case 401 | 403 | 404:
    return "Not allowed"

```

？不懂

```
我们可以向一个模式添加 if 子句，称为“约束项”。 如果约束项为假值，则 match 将继续尝试下一个 case 语句块。 请注意值的捕获发生在约束项被求值之前。
```

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```





## 类























如果用类组织数据，可以用“类名后接一个参数列表”这种很像构造器的形式，把属性捕获到变量里：

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
            
# 传参可以指定要传给哪个变量
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```



```
__match_args__是一个特殊的类属性，用于模式匹配（match-case语句）中的类模式匹配。它定义了在模式匹配中，可以用于解包对象的属性顺序。
```



```python
class Point:
    # 这个元组定义了在模式匹配中应该解包的属性。对于 Point 类来说，它指定了模式匹配时按顺序解包 x 和 y 属性。
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```



### 枚举



## 函数

```python
def 函数名(参数列表...):
    """文档字符串"""
    pass
# 将函数对象的引用给f
f=函数名
```

局部变量符号表

函数变量

内置名称符号表

函数定义在当前符号表中把函数名与**函数对象**关联在一起



**默认值**

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
```

**默认值在 *定义* 作用域里的函数定义中求值**,所以f()结果是5

```python
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
```

 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数：

```python
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
```

关键字形参也叫作命名形参



仅位置传参，仅关键字传参

```python
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```



 **任意实参列表**

参数前加*

**解包实参列表**

解包：将一个可迭代对象（如列表、元组或字符串）的元素直接赋值给多个变量

```python
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
```

`字典可以用 `**` 操作符传递关键字参数`



### Lambda 表达式

用于创建小巧的匿名函数,只是常规函数定义的语法糖





### 函数注解

函数标注: 以字典的形式存放在函数的 __annotations__ 属性

参数标注: 形参名后加冒号，后面跟一个会被求值为标注的值的表达式

返回值标注:  返回值标注的定义方式是加组合符号 `->`，后面跟一个表达式，这样的校注位于形参列表和表示 [`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 语句结束的冒号

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
```

## 数据结构



### 列表

del



### 元组

输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组。输入时，圆括号可有可无，不过经常是必须的

元组是 immutable （不可变的），一般可包含异质元素序列，通过解包（见本节下文）或索引访问（如果是 namedtuples，可以属性访问）。列表是 mutable （可变的），列表元素一般为同质类型，可迭代访问

```python
# 创建空元组
empty = ()
# 创建单个元素的元组
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

singleton
```



### 集合

集合是由不重复元素组成的无序容器

空集合只能用set()创建，因为{}表示空字典

```python

```



### 字典













# pandas



pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

**应用**

Pandas 可以让你轻松地处理各种数据结构，尤其是表格型数据

* 数据加载和保存：可以从各种数据源加载数据，包括 CSV 文件、Excel 表格、SQL 数据库、JSON 文件等
* 数据清洗：提供了丰富的函数和方法，用于数据清洗、处理缺失值、重复值、异常值等，以及进行数据转换、重塑和合并操作。
* 统计分析： 提供了各种统计函数和方法，用于描述性统计、聚合操作、分组运算、透视表等数据分析任务。
* 数据可视化：结合了 Matplotlib 库，可以轻松地进行数据可视化，绘制各种统计图表，如折线图、散点图、直方图等。



医疗保健：医疗保健领域需要处理和分析大量的医疗数据，包括患者数据、临床试验数据、医疗图像数据等。Pandas 提供了处理和分析这些数据的工具，支持医疗研究和临床决策。



## **数据结构**



### Series 

 类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成，

* 可以将 `Series` 视为带有索引的一维数组

- 索引可以是唯一的，但不是必须的，Pandas 将默认创建一个从 0 开始的整数索引
- 数据可以是标量、列表、NumPy 数组等

```python
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
```









### DataFrame

* 用于表示二维表格型数据,既有行索引也有列索引
* 可以被看做由 Series 组成的字典（共同用一个索引）
* 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作
* 处理缺失数据：DataFrame 可以包含缺失数据，Pandas 使用 NaN（Not a Number）来表示
* 时间序列支持：DataFrame 对时间序列数据有特别的支持，可以轻松地进行时间数据的切片、索引和操作。
* 滚动窗口和时间序列分析：支持对数据集进行滚动窗口统计和时间序列分析。

```python
# 构造方法
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

* DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame
* DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。

































