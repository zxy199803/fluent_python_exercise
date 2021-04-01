"""
协程中未处理的异常会向上冒泡，传给触发协程的对象
终止协程的一种方式:发送某个哨符值，让协程退出

显式把异常发给协程
    generator.throw(exc_type[,exc_value[,traceback]])
        使生成器在暂停的yield表达式处抛出指定的异常
    generator.close()
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


# my_avg = averager()
# print(my_avg.send('ad'))  # 协程内部没有处理异常，协程会终止
# print(my_avg.send(10))  # 如果试图重新激活协程，会抛出异常

class DemoException(Exception):
    """为这次演示定义的异常类型"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received:{!r}'.format(x))  # 如果没有异常显示接收到的值
    raise RuntimeError('This line should never run')  # 永远不会执行，只有未处理的异常才会终止无限循环，而一旦出现未处理异常，协程会立即终止


def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received:{!r}'.format(x))
    finally:  # 不管协程如何结束都做些清理工作
        print('-> coroutine ending')


exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)  # 处理了异常，协程继续
exc_coro.send(13)
exc_coro.throw(ZeroDivisionError)  # 传入无法处理的异常，协程终止
