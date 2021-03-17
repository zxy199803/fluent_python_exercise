"""
在每次调用被装饰的函数时计时，把经过的时间、传入的参数、调用结果打印

装饰器的典型行为：把被装饰函数替换成新函数，两种接受相同的参数，通常返回被装饰函数本该返回的值，同时还做一些额外的操作
"""
import time


#  缺点：不支持关键字参数，掩盖了被装饰函数的__name__和__doc__属性
def clock(func):
    def clocked(*args):  # 内部函数，接受任意个定位参数
        t0 = time.perf_counter()  # 记录初始时间t0
        result = func(*args)  # clocked的闭包中包含自由变量func  调用原来的函数，保存结果
        elapsed = time.perf_counter() - t0  # 计算经过时间
        name = func.__name__
        arg_str = ' '.join(repr(arg) for arg in args)  # repr()将对象转化为供解释器读取的形式
        print('[%0.8fs] %s(%s)  -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked  # 返回内部函数，取代被装饰的函数





import functools


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s)  -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked

@clock2
def snooze(seconds):
    time.sleep(seconds)


@clock2
def factorial(n):
    return n if n < 2 else n * factorial(n - 1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorical(6)')
    print('6!=', factorial(6))
