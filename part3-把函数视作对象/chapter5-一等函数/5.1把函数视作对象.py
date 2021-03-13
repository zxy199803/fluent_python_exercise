"""
Python中函数是一等对象
一等对象：
    在运行时创建
    能赋值给变量或函数结构中的元素
    能作为参数传给函数
    能作为函数的返回结果
Python中整数、字符串、字典都是一等对象

“把函数视为一等对象”简称为"一等函数"
"""


def factorial(n):
    """return n!!!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)  # __doc__属于用于生成对象的帮助文本
print(type(factorial))  # factorical 是 function类的实例

# 通过别的名称使用函数，再把函数作为参数传递
fact = factorial
print(fact)
fact(5)
print(map(factorial, range(11)))  # map(function, iterable, ...),function以参数序列中的每一个元素调用function函数
print(list(map(fact,range(11))))