"""
yield from x表达式对x做的第一件事是调用iter(x)从中获取迭代器
yield from 可替代产出值的嵌套for循环
yield from的主要作用是打开双向通道，把最外层的调用与最内层的子生成器连接起来，这样两者可以直接发送和产出值，还可以直接传入异常

委派生成器
    包含yield from <iterable>表达式的生成器函数
子生成器
    从yield from表达式中<iterable>获取的子生成器
调用方
    指代调用委派生成器的客户端代码

子生成器不暂停，委派生成器会在yield from表达式处永远暂停，程序不会向前执行（因yield from把控制权转交给客户端代码，即委派生成器的调用方了）

委派生成器相当于管道，可以把任意数量的委派生成器连接在一起。这个链条要以一个使用yield表达式的简单生成器结束，或以任何可迭代对象结束
任何yield from链条必须由客户驱动，在最外层委派生成器上调用next()函数或.send()方法
"""


def gen0():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def gen():
    yield from 'AB'
    yield from range(1, 3)


print(list(gen()))


# 使用yield from链接可迭代的对象
def chain(*iterables):  # itertools模块提供了优化版的chain函数，用C编写
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))

# 示例16-17
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:  # 终止条件很重要，否则调用这个协程的生成器会永远阻塞
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()  #返回值绑定到results[key]上


# 客户端代码，即调用方
def main(data):
    results = {}
    for key, values in data.items():  # 每次新建一个grouper实例
        group = grouper(results, key)  # group作为协程使用
        next(group)  # 预激委派生成器，此时进入while True循环，调用子生成器averager后，在yield from表达式暂停
        for value in values:
            group.send(value)  # value最终达到averager函数中的term = yield一行，grouper永远不知道传入的值是什么
        group.send(None)  # 终止子生成器
    print(results)
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, uint = key.split(';')
        print('{:2}{:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}
unit = 'kg'

main(data)
