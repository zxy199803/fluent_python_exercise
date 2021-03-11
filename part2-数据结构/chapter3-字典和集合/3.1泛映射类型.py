from collections import abc

"""
标准库里所有映射类型都是利用dict实现，因此只有可散列的数据类型才能做key

可散列的数据类型
    在该对象的生命周期中散列值不变，需要实现__hash__()方法
    有__eq__()方法，跟其他键值做比较
    
    可散列
        原子不可变数据类型(如str,bytes,数值)
        frozenset([iterable]) 返回一个冻结的集合，冻结的集合不能添加或删除任何元素
        所有元素都是可散列的元组。元组本身是不可变序列，但其元素可能是其他可变类型的引用
        用户自定义的类型的对象。散列值为id()函数的返回值，因此对象在比较的时候是不相等的
"""

my_dic = {}
print(isinstance(my_dic, abc.Mapping))
# 用isinstance检查某个参数是否为dict类型

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
#  print(hash(tl))  # TypeError: unhashable type: 'list'
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# 字典有多种构造方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
