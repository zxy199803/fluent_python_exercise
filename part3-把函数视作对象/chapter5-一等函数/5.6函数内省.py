"""
使用dir函数探知函数的属性

把函数视为对象相关的几个属性
__dict__
    函数使用__dict__属性存储赋予它的用户属性，相当于基本形式的注解
__call__
    实现()运算符，即可调用对象协议
"""


def factorial(n):
    """return n!!!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(dir(factorial))  # 大多数属性是Python对象共有的


# 函数专有而用户定义的一般对象没有的属性
class C: pass  # 创建空的用户定义的类


obj = C()  # 实例


def func(): pass  # 创建空的函数


print(sorted(set(dir(func)) - set(dir(obj))))  # 函数有而类的实例没有的属性
