"""
典型的迭代器模式的作用:遍历数据结构

内置的range函数生成有穷整数等差数列

itertools模块提供了19个生成器函数
    itertools.count 返回的生成器能生成多个数，不传入参数会生成从零开始的整数数列。该函数从不停止，调用list(count())会创建一个特别大的列表超出内存
    itertools.takewhile 生成一个使用另一个生成器的生成器，在指定的条件计算结果为False时停止

实现生成器时要知道标准库有什么可用，避免重复发明轮子
"""


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):  # 使用生成器函数实现特殊的__iter__方法
        result = type(self.begin + self.step)(self.begin)  # 把self.begin强制转换成加法算式得到的类型
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result  # 生成当前的result值
            index += 1  # 不直接使用self.step+result，降低处理浮点数时累计效性导致错误的风险
            result = self.begin + self.step * index  # 计算可能存在的下一个结果


import itertools

gen = itertools.count(1, .5)
print(next(gen))
print(next(gen))

gen1 = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(list(gen1))


def aritprog_gen(begin, step, end=None):  # 因定义体中没有yield不是生成器函数，它会返回一个生成器，是生成器函数工厂
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
