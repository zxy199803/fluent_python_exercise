"""
Python的函数是真正的对象，任何Python的对象都可以表现得像函数，只需实现实例方法__call__
实现__call__须在内部维护一个状态，让它在调用之间可用，如BingoCage中的剩余元素
"""
import random


class BingoCage:
    def __init__(self, items):  # 接受任何可迭代对象，在本地构建一个副本
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()  # 删除并返回最后一个元素
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # 设定错误消息

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))  # 实例
print(bingo.pick())
print(bingo())  # 实例作为函数调用
print(bingo())
print(bingo())
print(callable(bingo))
