"""
classmethod：定义操作类而不是操作实例的方法。classmethod改变了调用方法的方式，类方法的第一个参数是类本身而不是实例
最常见用途：定义备选构造方法

staticmethod (不是特别有用) 也会改变方法的调用方式，但第一个参数不是特殊的值。静态方法就是普通函数，在类的定义体中
"""
class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth())
print(Demo.klassmeth('spam'))  # 不管怎么调用Demo.klassmeth()，他的第一个参数始终是Demo类
print(Demo.statmeth())
print(Demo.statmeth('spam'))
s = Demo.klassmeth('spam')
