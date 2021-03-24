"""
Python数据模型的哲学是尽量支持基本协议
鉴于序列协议的重要性，如果没有__iter__和__contains__方法，Python会调用__getitem__方法，设法让迭代和in运算符可用
Python会特殊对待看起来像是序列的对象。为了迭代对象，解释器会尝试调用两个不同的方法
"""


class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
for i in f:  # 即使没有__iter__方法，Foo实例也是可迭代对象，因为发现有__getitem__方法
    print(i)
