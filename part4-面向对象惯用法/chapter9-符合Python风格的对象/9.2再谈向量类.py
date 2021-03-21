from array import array
import math


class Vector2d:
    __slots__ = ('__x','__y')  # 告诉解释器类中的所有实例属性。大规模数据应使用Numpy
    typecode = 'd'  # 类属性,在Vector2d实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.__x = float(x)  # 把x,y尽早转换成浮点数，尽早捕获错误
        self.__y = float(y)  # 使用两个前导下划线把属性标记为私有的

    @property
    def x(self):
        return self.__x

    @property  # 把读值方法标记为特性
    def y(self):  # 读值方法与公开属性同名
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))  # 将Vector2d实例变成可迭代对象，这样才能拆包

    def __repr__(self):
        class_name = type(self).__name__  # 便于修改typecode时候直接继承__repr__方法
        return '{}({!r},{!r})'.format(class_name, *self)  # Vector2d实例是可迭代对象，可以拆包

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(
            array(self.typecode, self))  # 把typecode转换成字节序列，然后迭代实例得到一个数组，再把数组转换成字节序列

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # 为快速比较所有分量，在操作中构建元组

    def __abs__(self):
        return math.hypot(self.x, self.y)  # 模长

    def __bool__(self):
        return bool(abs(self))  # 非零值是True

    # 备选构造方法
    @classmethod
    def frombytes(cls, octets):  # 不用传入self参数，通过cls传入类本身
        typecode = chr(octets[0])  # 第一个字节读取tpyecode
        memv = memoryview(octets[1:].cast(typecode))  # memoryview.cast 用不同的方式读写同一块内存数据，内容字节不会随意移动
        return cls(*memv)  # 使用cls参数构建了一个新的实例

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]  # 从中删除p后缀
            coords = (abs(self), self.angle())
            outer_fmt = '<{},{}>'
        else:
            coords = self
            outer_fmt = '({},{})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    # 将对象可散列
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)  # 使用位运算符异或(^)混合各分量的散列值


v1 = Vector2d(1, 2)
print(v1.x, v1.y)  # 可直接通过属性访问
x, y = v1
print(x)
print(x, y)
print(repr(v1))
print(bytes(v1))  # 实例的二进制表示形式
