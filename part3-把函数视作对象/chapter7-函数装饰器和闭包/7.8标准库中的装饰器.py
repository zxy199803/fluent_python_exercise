"""
使用functools.lru_cache做备忘,优化递归算法
它把耗时的函数结果保存起来，避免传入相同的参数时重复计算
lru(least recently used)，表明缓存不会无限制增长，一段时间不用的缓存条目会被丢掉

functools.lru_cache(maxsize=,typed=False) 有两个可选参数
    maxsize 指定存储多少个调用的结果，应设为2的幂
    typed 设为True，把不同参数类型得到的结果分开保存（浮点数和整数参数分开）

lru_cache使用字典存储结果，被其装饰的函数所有参数都必须是可散列的
"""
import functools
import time


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


@functools.lru_cache()
@clock2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(7))  #看出有多个重复调用
