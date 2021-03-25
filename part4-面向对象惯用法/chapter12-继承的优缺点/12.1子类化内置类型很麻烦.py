"""
子类化内置类型的缺点

内置类型可以子类化，但内置类型不会调用用户定义的子类覆盖的特殊方法。
这违背了面向对象编程的基本原则：应始终从实例(self)所属的类开始搜索方法
内置类型的方法调用其他类的方法，如果被覆盖了也不会被调用。
只发生在使用C语言实现的内置类型内部的方法委托上

子类化使用Python编写的类不受此影响
直接子类化内置类型容易出错。用户自己定义的类应该继承collections模块中的类，如UserDict等，这些类做了特殊设计易于扩展
"""
import collections


class DeppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)  # 把职责委托给超类


dd = DeppelDict(one=1)  # __init__方法继承自dict
print(dd)
dd['two'] = 2  # 调用了覆盖的__setitem__方法
print(dd)
dd.update(three=3)  # update方法继承自dict
print(dd)


class DeppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd2 = DeppelDict2(one=1)
print(dd2)

class AnswerDict(dict):
    def __getitem__(self, item):
        return 42


ad = AnswerDict(a='foo')
print(ad['a'])
print(ad)
d = {}
d.update(ad)  # 忽略了AnswerDict的__getitem__方法
print(d)
