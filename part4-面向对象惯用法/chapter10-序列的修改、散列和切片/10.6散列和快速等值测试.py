"""
functools.reduce()
思想：把一系列值规约成单个值
reduce(fn,lst)
    r1=fn(lst[0],lst[1])
    r2=fn(r1,lst[2])
    ...
    直到最后一个元素

异或运算：相同取0，相异取1

映射规约：把函数应用到各元素上产生新序列（映射，map），然后计算聚合值(规约，reduce)
"""
import functools

print(functools.reduce(lambda a, b: a * b, range(1, 6)))

# 计算整数0-5的累计异或的3种方式
n = 0
for i in range(1,6):
    n^=i
print(n)

print(functools.reduce(lambda a,b:a^b,range(6)))

import operator
print(functools.reduce(operator.xor,range(6)))  # operator模块以函数形式提供了Python中的全部中缀运算符