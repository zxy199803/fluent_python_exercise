"""
装饰器是函数，可以组合起来使用

@d1
@d2
def f():
    print('f')

等同于
def f():
    print('f')

f = d1(d2(f))
"""