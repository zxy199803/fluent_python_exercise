"""
functools.singledispatch 装饰器把整体方案拆分成多个模块
使用@singledispatch装饰的普通函数会变成泛函数：根据第一个参数的类型，以不同方式执行相同操作的一组函数
各个专门函数使用@base_function.register(type)装饰

singledispatch机制使得可以在系统的任何地方和任何模块中注册专门函数，以后可以轻松添加新的专门函数处理那个类型
可以为不是自己编写、不能修改的类添加自定义函数
"""
import html

# 生成html，显示不同类型的Python对象
# def htmlize(obj):
#     content = html.escape(repr(obj))
#     return '<pre>{}</pre>'.format(content)


# python不支持重载方法或函数，不能使用不同的签名定义htmlize的变体，也无法使用不同的方式处理不同的数据类型
# print(htmlize({1,2,3}))
# print(htmlize(abs))

from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch  # 标记处理object类型的基函数
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)  # numbers.Integral是int的虚拟超类，注册的专门函数应处理抽象基类，不要处理具体实现，这样代码支持的兼容类型更广泛
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)  # 可叠放多个装饰器，让同一函数支持不同类型
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
