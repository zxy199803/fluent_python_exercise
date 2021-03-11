"""
collections.OrderedDict
    添加键时保持顺序，其popitem方法删除并返回字典的最后一个元素

collections.ChainMap
    可容纳数个不同的映射对象

collections.Counter
    给键准备一个整数计数器，每次更新一个键时会增加这个计数器。
    可用于给可散列表对象计数、可当成多重集合(集合里元素可出现多次)使用
    most_common[n]按次序返回映射里最常见的n个键和他们的计数

collections.UserDict
    把标准的dict用纯python实现，给用户继承来写子类
"""
import collections
ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaazzzz')
print(ct)
print(ct.most_common(3))