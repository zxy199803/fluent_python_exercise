"""
python 唯一支持的参数传递模式 共享传参（call by sharing）：函数的各个形式参数获得实参中各个引用的副本，即函数内部的形参是实参的别名
共享传参使得函数可能对修改作为参数传入的可变对象，但不能修改对象的标识

不要使用可变类型作为参数的默认值
通常使用None作为接收可变值的参数的默认值
默认值在定义函数时计算，默认值变成了函数对象的属性

设计接口的最佳实现：最小惊讶原则

在类中直接把参数赋值给实例变量要三思，这样会为参数对象创建别名。如果不确定就创建副本

list()构造方法接受任何可迭代对象
"""
# 函数可能会修改接收到的任何可变对象

def f(a, b):
    a += b
    return a


a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a)  # 列表变了
c = (5,6)
d = (7,8)
print(f(c,d))
print(c)  # 元组没变

class HauntedBus:
    def __init__(self,passengers=[]):  # 没有用None,用了空列表
            self.passengers = passengers  # 没有指定初始乘客的HauntedBus实例会共享一个乘客列表。self.passengers 变成 passengers的别名

    def pick(self,name):
        self.passengers.append(name)

    def deop(self,name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
bus1.pick('Charlie')
bus1.deop('Alice')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)