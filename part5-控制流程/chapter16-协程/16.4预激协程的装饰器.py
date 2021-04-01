"""
如果不预激，那么协程没什么用。为了简化协程用法，有时会使用一个预激装饰器
"""
from functools import wraps


def coroutine(func):
    """装饰器：向前执行到第一个yield表达式，预激func"""

    @wraps(func)  # 旨在消除装饰器对原函数造成的影响，即对原函数的相关属性进行拷贝，已达到装饰器不修改原函数的目的
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average  #
        total += term
        count += 1
        average = total / count

my_avg = averager()
print(my_avg.send(10))