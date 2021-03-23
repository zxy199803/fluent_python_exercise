"""
序列类型的构造方法最好接受可迭代对象为参数
"""
from array import array
import reprlib
import math
import numbers


class Vector:
    typecpde = 'd'

    def __init__(self, components):
        self._components = array(self.typecpde, components)  # array效率比List高，其背后存的是字节表述。受保护对象

    def __iter__(self):
        return iter(self._components)  # 返回可迭代对象

    def __repr__(self):  # 用于调试，绝对不能抛出异常，尽量输出有用内容让用户能识别目标对象
        components = reprlib.repr(self._components)  # reprlib.repr函数用于生成大型结构的安全表示形式，限制输出字符串的长度
        components = components[components.find('['):-1]  # 否则变成Vector(array('d', [3.0, 4.0,5.0))，
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecpde)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):  # 不用传入self参数，通过cls传入类本身
        typecode = chr(octets[0])  # 第一个字节读取tpyecode
        memv = memoryview(octets[1:].cast(typecode))  # memoryview.cast 用不同的方式读写同一块内存数据，内容字节不会随意移动
        return cls(memv)

    # 可切片的序列
    def __len__(self):
        return len(self._components)

    # 此版本不能处理切片
    # def __getitem__(self, index):
    #     return self._components[index]

    # 能处理切片
    def __getitem__(self, index):
        cls = type(self)  # 返回对象的类型
        if isinstance(index, slice):  # 若index参数的值是slice对象
            return cls(self._components[index])  # 构造新的Vector类
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))


v1 = Vector([3, 4, 5])
print(len(v1))

print(v1)
print(v1[0])
print(v1[1:3])  # 不完美，希望Vector实例的切片也是Vector实例
