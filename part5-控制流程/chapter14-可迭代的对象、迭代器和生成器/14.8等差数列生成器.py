"""
典型的迭代器模式的作用:遍历数据结构

内置的range函数生成有穷整数等差数列

itertools模块提供了19个生成器函数
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
