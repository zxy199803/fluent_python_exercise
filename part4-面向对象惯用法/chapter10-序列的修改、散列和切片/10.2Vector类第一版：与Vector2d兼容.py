"""
序列类型的构造方法最好接受可迭代对象为参数
"""
from array import array
import reprlib
import math


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
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):  # 不用传入self参数，通过cls传入类本身
        typecode = chr(octets[0])  # 第一个字节读取tpyecode
        memv = memoryview(octets[1:].cast(typecode))  # memoryview.cast 用不同的方式读写同一块内存数据，内容字节不会随意移动
        return cls(memv)