"""
获取协程的返回值要绕个圈子
yield from结构会在内部自动捕获StopIteration异常，把value属性的值变成yield from表达式的值
在函数外部使用yield from及yield会导致句法出错
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break  # 为了返回值，协程必须正常终止
        total += term
        count += 1
        average = total/count
    return Result(count,average)

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
# coro_avg.send(None)  # 生成器对象会抛出StopIteration异常，异常对象的value属性值保存着返回的值
try:  # 捕获异常，获取返回值
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value