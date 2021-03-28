"""
复制列表：构造方法list()和[:]均是浅复制（复制了最外层的容器，副本中的元素是源容器中元素的引用）

对可变对象来说，+=就地修改
对元组来说，+=创建一个新的元组

深复制：副本不共享内部对象的引用。copy模块的deepcopy
深复制有时可能太深了，可以实现特殊方法__copy__()和__deepcopy__()控制copy和deepcopy的行为
"""
l1 = [3, [4, 5]]
l2 = list(l1)
print(l2)
print(l1 is l2)  # 副本与源列表相等，但指代不同对象
l1.append(7)
print(l1)
print(l2)

l1 = [3, [4, 5], (7, 8, 9)]
l2 = list(l1)  # 两者引用了同一个列表和元组
l1.append(100)
l1[1].remove(4)
print("l1", l1)
print('l2', l2)
l2[1] += [33, 44]
l2[2] += (10, 11)  # l2[2] = l2[2] + （10，11）
print("l1", l1)
print('l2', l2)


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def deop(self, name):
        self.passengers.remove(name)


import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))  # 三个不同的Bus实例
bus1.deop('Bill')
print(bus2.passengers)  # bus1,bus2共享一个参数列表
print(bus3.passengers)

# deepcopy处理循环引用
a = [1, 2]
b = [a, 30]
a.append(b)
print(a)
