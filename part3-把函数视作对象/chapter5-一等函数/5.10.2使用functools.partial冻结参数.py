"""
functools.partial 用于部分应用一个函数。
部分应用：基于一个函数创建一个新的可调用对象，把原函数的某些参数固定
使用这个函数可以接受一个或多个参数的函数改编成需要回调的API，这样参数更少

functools.partialmethod：用于处理方法
"""
# partial把一个需要两个参数的函数改编成需要单参数的
from operator import mul
from functools import partial

triple = partial(mul, 3)  # 把第一个参数固定为3
print(triple(7))
print(list(map(triple, range(1, 10))))
